##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import transaction

from Shared.DC.ZRDB.TM import TM
from ZODB.POSException import TransactionFailedError

import logging

LOG = logging.getLogger("ZMySQLDA")


class joinTM(TM):

    _registered = False
    _finalize = False

    def _register(self):
        """ Override to replace transaction register() call with join().

            The primary reason for this is to eliminate issues in both the
            super's _register() and transaction register(). The former has a
            bare except: that hides useful errors. The latter deals poorly with
            exceptions raised from the join due to state modifications made
            before the join attempt.

            They also both (for our purposes) needlessly add wrapper objects
            around self, resulting in unnecessary overhead.
        """
        if not self._registered:
            try:
                transaction.get().join(self)
            except TransactionFailedError:
                msg = "database connection failed to join transaction."
                LOG.error(msg)
            except ValueError:
                msg = "database connection failed to join transaction."
                LOG.error(msg, exc_info=True)
                raise
            else:
                self._begin()
                self._registered = True
                self._finalize = False
