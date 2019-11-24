import requests
from datetime import date, timedelta, datetime
from AuthError import AuthError

class georide_cli:
    def getPositions(self, token, trackerID, startDate, endDate):
        url = "https://api.georide.fr/tracker/%s/trips/positions" % (trackerID)
        payload = {"from": startDate, "to": endDate}
        requestHeaders = {"Authorization": "Bearer %s" % (token)}
        r = requests.get(url, params=payload, headers=requestHeaders)
        if r.status_code == 401:
            raise AuthError("Token or trackerID not correct")
        return r.json()
    
    def getTrips(self, token, trackerID, startDate, endDate):
        url = "https://api.georide.fr/tracker/%s/trips" % (trackerID)
        endDate = ((endDate + timedelta(days=1)).strftime("%Y%m%d")) + "T015959"
        payload = {"from": startDate.strftime("%Y%m%d") + "T020000", "to": endDate}
        requestHeaders = {"Authorization": "Bearer %s" % (token)}
        r = requests.get(url, params=payload, headers=requestHeaders)
        if r.status_code == 401:
            raise AuthError("Token or trackerID not correct")
        return r.json()

    def getNewToken(self, user, password):
        url = "https://api.georide.fr/user/login"
        payload = {"email": user, "password": password}
        r = requests.post(url, data=payload)
        if r.status_code == 403:
            raise AuthError("User or/and password not correct")
        return r.json()["authToken"]

    def getTrackersID(self, token):
        requestHeaders = {"Authorization": "Bearer %s" % (token)}
        r = requests.get(
            "https://api.georide.fr/user/trackers", headers=requestHeaders
        )
        if r.status_code == 401:
            raise AuthError("Token or trackerID not correct")
        ret = []
        for tracker in r.json():
            ret.append([tracker["trackerId"], tracker["trackerName"]])
        return ret

    def revokeToken(self, token):
        url = "https://api.georide.fr/user/logout"
        requestHeaders = {"Authorization": "Bearer %s" % (token)}
        r = requests.post(url, headers=requestHeaders)
        return r.status_code