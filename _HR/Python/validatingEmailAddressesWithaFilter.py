#!/bin/python
# http://hr.gs/acfafc

def fun(s):
    # return True if s is a valid email, else return False
    result = False
    try: 
        e = s.split('@')
        id, host = e[0], e[1]
        id = id.replace('-','').replace('_','')
        if id.isalnum():
            try: 
                h = host.split('.')
                if len(h) != 2:
                    pass
                elif len(h[1]) < 1 or len(h[1]) > 3:
                    pass
                elif h[0].isalnum() and h[1].isalnum():
                    result = True
                else:
                    pass
            except:
                pass
        else:
            pass
    except:
        pass
    return result

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails