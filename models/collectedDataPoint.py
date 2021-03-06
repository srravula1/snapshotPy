from database import connect
import uuid as uuidpkg
import psycopg2.extras


class CollectedDataPoint:
    def __init__(self, variableHandle=None, timeFrame=None, value=None, organization_uuid=None, uuid=None,
                 interaction_uuid=None, variable_uuid=None):
        self.variableHandle = variableHandle
        self.timeFrame = timeFrame
        self.value = value
        self.organization_uuid = organization_uuid
        self.uuid = uuidpkg.uuid4() if uuid is None else uuid
        self.interaction_uuid = interaction_uuid
        self.variable_uuid = variable_uuid

        psycopg2.extras.register_uuid()

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO collectedDataPoints (variableHandle, timeFrame, value, organization_uuid, uuid, '
                    'interaction_uuid, variable_uuid) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (self.variableHandle, self.timeFrame, self.value, self.organization_uuid, self.uuid,
                     self.interaction_uuid, self.variable_uuid))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM collectedDataPoints WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
