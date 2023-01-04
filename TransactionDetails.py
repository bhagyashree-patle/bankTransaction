import random
from datetime import datetime
from datetime import date


class TransactionDetails:

    def custId(self):
        # generate random customer ID
        return random.randint(1, 100000)

    #def transId(self):
        # generate random transaction ID
      #  return random.randint(1**4, 10**4)

    # select transaction type
    def getTransType(self):

        transaction_type = ["Credit", "Debit"]
        trans_type = random.choice(transaction_type)
        return trans_type

    # select transaction details
    def getTransDetails(self):
        transaction_details = ["Cash", "ATM", "Online", "UPI"]
        trans_details = random.choice(transaction_details)
        return trans_details

    # generate random time of transaction
    def randomTime(self,date1,date2):
        """ This function will return a random datetime between two datetime objects. """
        d1 = datetime.strptime(date1, '%d/%m/%Y')
        d2 = datetime.strptime(date2, '%d/%m/%Y')
        year = random.randint(d1.year, d2.year)
        month = random.randint(d1.month, d2.month)
        day = random.randint(d1.day, d2.month)
        create_date = datetime(year, month, day)
        return create_date

    def getTransAmount(self):
        return random.randint(10, 500000)

    def getBalAmount(self, trans_amount, trans_type):

        if trans_type == 'Credit':
            final_bal = open_bal + trans_amount
        else:
            final_bal = open_bal - trans_amount
        # print(open_bal, trans_amount, trans_type,final_bal)
        return final_bal

        # return random.randint(10, 5000)

    def getMessage(self, trans_amount, open_bal, trans_type):
        # balance = 0
        # message = ["Transaction Successful", "Transaction failed"]
        if trans_type == 'Debit':
            if trans_amount <= open_bal:
                bal_amount = transactiondetails.getBalAmount(trans_amount, trans_type)
                # print("Transaction Successful")
                outmessage = "Transaction Successful"
            else:
                # print("Transaction failed")
                outmessage = "Transaction Failed"
                bal_amount = open_bal
        elif trans_type == 'Credit':
            bal_amount = transactiondetails.getBalAmount(trans_amount, trans_type)
            # print("Transaction Successful")
            outmessage = "Transaction Successful"

        return [str(bal_amount),(outmessage)]

counter = 0
while counter <= 1000000:
    transactiondetails = TransactionDetails()
    #transaction_id = transactiondetails.transId()
    transaction_id = counter
    cust_id = transactiondetails.custId()
    trans_type = transactiondetails.getTransType()
    trans_details = transactiondetails.getTransDetails()
    open_bal = random.randint(1000, 5000000)
    trans_amount = transactiondetails.getTransAmount()
    # bal_amount = transactiondetails.getBalAmount(trans_amount,trans_type)
    # print("Balance amount is:" ,bal_amount)
    created_time = transactiondetails.randomTime('01/01/2000', '31/12/2022')
    message = transactiondetails.getMessage(trans_amount, open_bal,trans_type)
    # print(message)
    # balance = transactiondetails.getMessage(trans_amount, open_bal,trans_type)
    flat_list = []
    for element in message:
        flat_list.append(element)


    transaction_details_list = [str(transaction_id),str(cust_id),trans_type,trans_details,str(trans_amount),
                                str(open_bal),created_time.strftime("%m/%d/%Y")]

    trans_details_final_list = transaction_details_list + flat_list


    final_trans_details = ','.join(trans_details_final_list)


    with open('D:/AWS Interview preparation/transactiondetails1.csv','a') as file:
         file.write(final_trans_details + '\n')
         file.close()

    counter += 1
print("Data has been written successfully")