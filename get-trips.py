# cli.py
import click
from georide import georide_cli
from AuthError import AuthError

from datetime import date, timedelta, datetime
import os, glob, json
import xml.etree.ElementTree as ET
from datetime import datetime


@click.command()
@click.argument('tracker_id')
@click.argument('start_date')
@click.argument('end_date')
@click.option('--username', '-u')
@click.option('--password', '-p')
@click.option('--token', '-t')
def main(tracker_id, start_date, end_date, username, password, token):
    georide = georide_cli()
    startDate = datetime.strptime(start_date, "%Y/%m/%d")
    endDate = datetime.strptime(end_date, "%Y/%m/%d")

    if(not token):
        if not (username and password):
            raise AuthError("Script require token or username and password")
        token = georide.getNewToken(username, password)

    trips=georide.getTrips(token, tracker_id, startDate, endDate)
    for trip in trips:
        startDateTrip = trip['startTime']
        endDateTrip = trip['endTime']
        positions = georide.getPositions(token, tracker_id, startDateTrip, endDateTrip)
        
        root = ET.Element('gpx')
        root.set('creator','Jules LE BRIS')
        root.set('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
        root.set('xsi:schemaLocation','http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd')
        root.set('version','1.1')
        root.set('xmlns','http://www.topografix.com/GPX/1/1')
        metadata = ET.SubElement(root, 'metadata')
        time = ET.SubElement(metadata, 'time')
        time.text = str(positions[0]['fixtime'])
        trk = ET.SubElement(root, 'trk')
        name = ET.SubElement(trk, 'name')
        name.text = str(positions[0]['fixtime'])[:-5]
        typeE = ET.SubElement(trk, 'type')
        typeE.text = "9"

        trkseg = ET.SubElement(trk, 'trkseg')
        for position in positions:
            #startLoop
            trkpt = ET.SubElement(trkseg, 'trkpt')
            trkpt.set('lat', str(position['latitude']))
            trkpt.set('lon', str(position["longitude"]))
            ele = ET.SubElement(trkpt, 'ele')
            ele.text = str(position["altitude"])
            time = ET.SubElement(trkpt, 'time')
            time.text = str(position["fixtime"])
            #fin de loop

        mydata = ET.tostring(root, encoding='utf8', method='xml')
        filename = (positions[0]['fixtime'][:-5]).replace(":", "-")
        myfile = open(filename+".gpx", "w")
        myfile.write(mydata.decode("utf-8"))

if __name__ == "__main__":
    main()