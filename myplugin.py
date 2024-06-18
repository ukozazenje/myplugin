from tutormfe.hooks import MFE_APPS
from tutor import hooks

@MFE_APPS.add()
def _remove_mfes(mfes):
    # Remove mfes
    for mfe in ["account", "profile", "communications", "course-authoring", "discussions", "gradebook", "learner-dashboard", "learning", "ora-grading"]:
        mfes.pop(mfe, None)
    return mfes

@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["authn"] = {
        "repository": "https://github.com/ukozazenje/frontend-app-authn.git",
        "port": 1999,
        "version": "testing", # optional, will default to the Open edX current tag.
    }
    return mfes

