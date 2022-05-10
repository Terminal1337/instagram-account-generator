import httpx


def getMail():
    response = httpx.get('https://api.kopeechka.store/mailbox-get-email?api=2.0&spa=1&site=instagram.com&sender=instagram&regex=&mail_type=hotmail.com&token=7dacff814a2423215374caeba3f7e011').json()
    return response

def getLetter(id):
    r = httpx.get('http://api.kopeechka.store/mailbox-get-message?full=1&id='+id+'&token=7dacff814a2423215374caeba3f7e011&type=JSON&api=2.0').json()
    r = r['value']
    return r
def getLetterx(id):
    tries = 0
    while tries < 30:
        time.sleep(2)
        value = CheckMail(id)
        if value != 'WAIT_LINK':
            tries += 1
            return value.replace('\\', '')
        return False