"""
Bite 163. Which packages were upgraded?

In this Bite you compare a list of packages (aka requirement.txt) from before vs. after (pip) upgrade.
Check the TESTS tab for the format of the input data.

Complete the changed_dependencies function that receives the old and new requiements (multiline)
strs and returns a list of package names that were upgraded (new version > previous version).

To keep it manageable you can assume that both requirement strs have the same packages,
no packages were added or deleted.

A note about the digits (major/minor) numbers in the packages:
they are ints, so twilio==6.23.1 > twilio==6.3.0 (see also Twilio's history log).
"""

from distutils.version import StrictVersion


def _extract_req_dict(reqs: str) -> dict:
    return dict(
        s.split('==')
        for s in reqs.strip().splitlines()
    )

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = _extract_req_dict(old_reqs)
    new = _extract_req_dict(new_reqs)

    return [name
            for name, version in old.items()
            if StrictVersion(new[name]) > StrictVersion(version)]
