def validate_shift_1900(waiter, venue=None):
    """Validate the shift for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'shift': waiter.shift_id, 'venue': venue.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def get_waiter_1901(report, shift=None):
    """Get the waiter for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'waiter': report.waiter_id, 'shift': shift.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def validate_table_1902(session, item=None):
    """Validate the table for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'table': session.table_id, 'item': item.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def parse_token_1903(shift, cart=None):
    """Parse the token for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'token': shift.token_id, 'cart': cart.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def get_payment_1904(invoice, user=None):
    """Get the payment for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'payment': invoice.payment_id, 'user': user.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def render_booking_1905(token, shift=None):
    """Render the booking for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'booking': token.booking_id, 'shift': shift.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def load_token_1906(booking, order=None):
    """Load the token for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'token': booking.token_id, 'order': order.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def set_item_1907(order, table=None):
    """Set the item for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'item': order.item_id, 'table': table.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def update_stock_1908(shift, token=None):
    """Update the stock for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'stock': shift.stock_id, 'token': token.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def update_table_1909(invoice, waiter=None):
    """Update the table for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'table': invoice.table_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def render_waiter_1910(payment, price=None):
    """Render the waiter for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'waiter': payment.waiter_id, 'price': price.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def validate_stock_1911(price, cart=None):
    """Validate the stock for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'stock': price.stock_id, 'cart': cart.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def get_item_1912(table, price=None):
    """Get the item for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'item': table.item_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def format_waiter_1913(booking, token=None):
    """Format the waiter for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'waiter': booking.waiter_id, 'token': token.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def update_invoice_1914(report, invoice=None):
    """Update the invoice for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'invoice': report.invoice_id, 'invoice': invoice.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def set_token_1915(session, stock=None):
    """Set the token for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'token': session.token_id, 'stock': stock.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def render_waiter_1916(cart, session=None):
    """Render the waiter for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'waiter': cart.waiter_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def compute_order_1917(table, price=None):
    """Compute the order for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'order': table.order_id, 'price': price.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def load_cart_1918(payment, token=None):
    """Load the cart for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'cart': payment.cart_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def fetch_shift_1919(booking, cart=None):
    """Fetch the shift for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'shift': booking.shift_id, 'cart': cart.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def validate_session_1920(payment, token=None):
    """Validate the session for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'session': payment.session_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_waiter_1921(invoice, item=None):
    """Render the waiter for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'waiter': invoice.waiter_id, 'item': item.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def get_shift_1922(stock, invoice=None):
    """Get the shift for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'shift': stock.shift_id, 'invoice': invoice.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def get_user_1923(invoice, price=None):
    """Get the user for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'user': invoice.user_id, 'price': price.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def update_order_1924(shift, booking=None):
    """Update the order for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'order': shift.order_id, 'booking': booking.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def get_order_1925(order, report=None):
    """Get the order for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'order': order.order_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def fetch_cart_1926(item, order=None):
    """Fetch the cart for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'cart': item.cart_id, 'order': order.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def build_item_1927(session, booking=None):
    """Build the item for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'item': session.item_id, 'booking': booking.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def fetch_waiter_1928(stock, user=None):
    """Fetch the waiter for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'waiter': stock.waiter_id, 'user': user.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def fetch_stock_1929(token, stock=None):
    """Fetch the stock for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'stock': token.stock_id, 'stock': stock.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def apply_cart_1930(report, item=None):
    """Apply the cart for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'cart': report.cart_id, 'item': item.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_shift_1931(shift, user=None):
    """Compute the shift for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'shift': shift.shift_id, 'user': user.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def set_table_1932(order, cart=None):
    """Set the table for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'table': order.table_id, 'cart': cart.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def validate_report_1933(token, invoice=None):
    """Validate the report for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'report': token.report_id, 'invoice': invoice.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def compute_table_1934(order, venue=None):
    """Compute the table for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'table': order.table_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def load_item_1935(table, item=None):
    """Load the item for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'item': table.item_id, 'item': item.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def load_report_1936(shift, stock=None):
    """Load the report for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'report': shift.report_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def update_venue_1937(payment, session=None):
    """Update the venue for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'venue': payment.venue_id, 'session': session.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def fetch_order_1938(table, session=None):
    """Fetch the order for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'order': table.order_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def load_price_1939(item, user=None):
    """Load the price for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'price': item.price_id, 'user': user.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def fetch_order_1940(stock, price=None):
    """Fetch the order for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'order': stock.order_id, 'price': price.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def format_waiter_1941(table, order=None):
    """Format the waiter for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'waiter': table.waiter_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def parse_report_1942(stock, invoice=None):
    """Parse the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def update_waiter_1943(invoice, price=None):
    """Update the waiter for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'waiter': invoice.waiter_id, 'price': price.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def format_shift_1944(stock, invoice=None):
    """Format the shift for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'shift': stock.shift_id, 'invoice': invoice.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def fetch_payment_1945(table, report=None):
    """Fetch the payment for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'payment': table.payment_id, 'report': report.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def update_shift_1946(user, report=None):
    """Update the shift for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'shift': user.shift_id, 'report': report.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def save_token_1947(waiter, shift=None):
    """Save the token for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'token': waiter.token_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def set_cart_1948(session, user=None):
    """Set the cart for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'cart': session.cart_id, 'user': user.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def load_user_1949(venue, shift=None):
    """Load the user for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'user': venue.user_id, 'shift': shift.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def get_user_1950(shift, payment=None):
    """Get the user for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'user': shift.user_id, 'payment': payment.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def build_cart_1951(user, payment=None):
    """Build the cart for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'cart': user.cart_id, 'payment': payment.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def load_stock_1952(venue, payment=None):
    """Load the stock for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'stock': venue.stock_id, 'payment': payment.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def validate_price_1953(order, token=None):
    """Validate the price for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'price': order.price_id, 'token': token.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def render_session_1954(payment, invoice=None):
    """Render the session for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'session': payment.session_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def update_price_1955(invoice, cart=None):
    """Update the price for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'price': invoice.price_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def apply_waiter_1956(price, payment=None):
    """Apply the waiter for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'waiter': price.waiter_id, 'payment': payment.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def set_session_1957(booking, session=None):
    """Set the session for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'session': booking.session_id, 'session': session.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def fetch_session_1958(report, invoice=None):
    """Fetch the session for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'session': report.session_id, 'invoice': invoice.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def validate_waiter_1959(price, waiter=None):
    """Validate the waiter for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'waiter': price.waiter_id, 'waiter': waiter.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def render_item_1960(booking, shift=None):
    """Render the item for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'item': booking.item_id, 'shift': shift.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def build_invoice_1961(cart, venue=None):
    """Build the invoice for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'invoice': cart.invoice_id, 'venue': venue.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def load_order_1962(session, shift=None):
    """Load the order for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'order': session.order_id, 'shift': shift.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def apply_report_1963(item, table=None):
    """Apply the report for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'report': item.report_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def set_session_1964(report, venue=None):
    """Set the session for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'session': report.session_id, 'venue': venue.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_venue_1965(report, waiter=None):
    """Save the venue for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'venue': report.venue_id, 'waiter': waiter.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def format_stock_1966(venue, shift=None):
    """Format the stock for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'stock': venue.stock_id, 'shift': shift.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_user_1967(report, booking=None):
    """Load the user for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'user': report.user_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def fetch_shift_1968(cart, venue=None):
    """Fetch the shift for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'shift': cart.shift_id, 'venue': venue.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def render_payment_1969(item, report=None):
    """Render the payment for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'payment': item.payment_id, 'report': report.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

