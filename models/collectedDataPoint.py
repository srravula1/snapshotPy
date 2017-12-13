from database import connect

class CollectedDataPoint:
    def __init__(self, variableHandle=None, timeFrame=None, value=None, organization_uuid=None, uuid=None, interactionMaterial_uuid=None):
        self.variableHandle = variableHandle
        self.timeFrame = timeFrame
        self.value = value
        self.organization_uuid = organization_uuid
        self.uuid = uuid
        self.interactionMaterial_uuid = interactionMaterial_uuid

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO collectedDataPoints (variableHandle, timeFrame, value, organization_uuid, '
                    'interactionMaterial_uuid) VALUES (%s, %s, %s, %s, %s)',
                    (self.variableHandle, self.timeFrame, self.value, self.organization_uuid,
                     self.interactionMaterial_uuid))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM collectedDataPoints WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6])