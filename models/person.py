from database import connect
import uuid
import psycopg2.extras


class Person:
    def __init__(self, called=None, givenName=None, surName=None, maidenName=None, gender=None, birthDate=None,
                 uuid=uuid.uuid4(), hasUserAccount=False, isTeamMember=False):
        self.called = called
        self.givenName = givenName
        self.surName = surName
        self.maidenName = maidenName
        self.gender = gender
        self.birthDate = birthDate
        self.uuid = uuid
        self.hasUserAccount = hasUserAccount
        self.isTeamMember = isTeamMember

        psycopg2.extras.register_uuid()

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO persons (called, givenName, surName, maidenName, gender, birthDate, uuid, '
                    'hasUserAccount, isTeamMember) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (self.called, self.givenName, self.surName, self.maidenName, self.gender, self.birthDate,
                     self.uuid, self.hasUserAccount, self.isTeamMember))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM persons WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])