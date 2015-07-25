from __future__ import print_function
import json
import sys


global pay_person
global recv_person
global money
global action

pay_person = ''
recv_person = ''
money = 0
action = ''

global billLog
global resultLog
global result

billLog = open('bill.log', "a+")
resultLog = open('result.log', "r")
result = json.load(resultLog)
resultLog.close()

resultLog = open('result.log', "w")


def parse_args(args):

    global pay_person
    global recv_person
    global money
    global action

    parsed = False

    if len(args) == 2:
        #bill.py xxx
        if args[1] == 'show':
            action = 'show'

            parsed = True

    if len(args) == 4 and args[2] == 'out':
        #bill.py SomeOne out SomeMoney
        pay_person = args[1]
        money = args[3]
        action = 'out'

        parsed = True

    if len(args) == 5 and args[2] == 'to':
        #bill.py SomeOne1 to SomeOne2 SomeMoney
        pay_person= args[1]
        recv_person = args[3]
        money = args[4]
        action = 'to'

        parsed = True


    if not parsed:
        print("args Error, Please read the README.md for correct args!")
        sys.exit()

def logBill():

    global billLog
    global resultLog
    global result

    log = {'pay_peron': pay_person,
           'recv_person': recv_person,
           'money': money}
    billLog.write(json.dumps(log))


def main(args):

    parse_args(args)

    print(action)

    if action == 'show':
        all_out_money = 0
        recv_people = []
        pay_people = []

        for person in result:
            all_out_money += result[person]
        for person in result:
            if result[person] > all_out_money / 3:
                recv_people.append((person, result[person] - all_out_money / 3))
            if result[person] < all_out_money / 3:
                pay_people.append((all_out_money / 3 - person, result[person]))

        i = 0
        recv_item = recv_people[i]
        for pay_item in pay_people:
            while pay_item[1] > recv_item[1]:
                pay_item[1] -= recv_item[1]
                print("%s pay %s %s" % (pay_item[0], recv_item[0], recv_item[1]))
                i += 1
                if i > len(recv_people):
                    print("%s pay NoOne %s" % (pay_item[0], pay_item[1]))
                    recv_item[1] = 0
                    break
                recv_item = recv_people[i]
            if pay_item[1] < recv_item[1]:
                recv_item[1] -= pay_item[1]
                print("%s pay %s %s" % (pay_item[0], recv_item[0], pay_item[1]))

    if action == 'out':
        result[pay_person] += int(money)
        resultLog.write(json.dumps(result))
        logBill()

    if action == 'to':
        result[pay_person] += int(money)
        result[recv_person] -= int(money)
        resultLog.write(json.dumps(result))
        logBill()


    resultLog.close()
    billLog.close()


if __name__ == '__main__':
    main(sys.argv)
