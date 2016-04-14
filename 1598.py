'''
Data - queue
1598 Exchange

Order book receives a stream of messages. Messages are orders and requests to cancel previously issued orders. Orders that were not cancelled are called active. There are orders to buy and orders to sell. Each order to buy or to sell has a positive size and a positive price. Order book maintains a list of active orders and generates quotes and trades. Active order to buy at the highest price is the best buy order and its price is called bid price. Active order to sell at the lowest price is the best sell order and its price is called ask price. Ask price is always lower than bid price, that is, buyers are willing to pay less than sellers want to receive in return.

If an order to buy arrives to the order book at a price greater or equal to the current ask price, then the corresponding orders are matched and trade happens — buyer and seller reached agreement on a price. Vice versa, if an order to sell arrives to the order book at a price less or equal to the current bid price, then trade happens, too. For the purpose of order matching, order book works like a FIFO queue for orders with the same price (read further for details).

Input

The input will contain several test cases, each of them as described below. Consecutive test cases are separated by a single blank line.  The first line of the input contains a single integer number n (1 ≤ n ≤ 10000) — the number of incoming messages that the order book has to process. The following n lines contain messages. Each line starts with a word describing the message type — ‘BUY’, ‘SELL’, or ‘CANCEL’ followed after a space by the message parameters.
‘BUY’ and ‘SELL’ denote an order to buy or to sell correspondingly, and are followed by two integers q and p (1 ≤ q ≤ 99999, 1 ≤ p ≤ 99999) — order size and price. ‘CANCEL’ denotes a request to cancel previously issued order. It is followed by a single integer i which is the number of the message with some preceding order to buy or to sell (messages are numbered from 1 to n).

Output

For each test case, the output must follow the description below. The outputs of two consecutive cases will be separated by a blank line.  Write to the output a stream of quotes and trades that the incoming messages generate. For every trade write ‘TRADE’ followed after space by the trade size and price. For every quote write ‘QUOTE’ followed after space by the quote bid size, bid price, minus sign (‘-’), ask size, ask price (all separated by spaces).
There is a special case when there are no active orders to buy or to sell in the order book (bid and/or ask are not defined). This case is treated as follows. If there is no active order to buy, then it is assumed that bid size is zero and bid price is zero. If there is no active order to sell, then it is assumed that ask size is zero and ask price is 99 999. Note, that zero is not a legal price, but 99 999 is a legal price. Recipient of quote messages distinguishes actual 99 999 ask price from the special case of absent orders to sell by looking at its ask size.
'''

