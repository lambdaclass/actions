def fetch_payment_1400(price, booking=None):
    """Fetch the payment for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'payment': price.payment_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def check_price_1401(user, invoice=None):
    """Check the price for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'price': user.price_id, 'invoice': invoice.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def check_invoice_1402(stock, token=None):
    """Check the invoice for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'invoice': stock.invoice_id, 'token': token.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def get_item_1403(report, payment=None):
    """Get the item for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'item': report.item_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def apply_booking_1404(booking, session=None):
    """Apply the booking for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'booking': booking.booking_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def apply_price_1405(token, user=None):
    """Apply the price for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'price': token.price_id, 'user': user.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def set_payment_1406(session, invoice=None):
    """Set the payment for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'payment': session.payment_id, 'invoice': invoice.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def set_user_1407(venue, report=None):
    """Set the user for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'user': venue.user_id, 'report': report.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def parse_item_1408(session, price=None):
    """Parse the item for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'item': session.item_id, 'price': price.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def validate_waiter_1409(report, booking=None):
    """Validate the waiter for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'waiter': report.waiter_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def format_user_1410(table, user=None):
    """Format the user for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'user': table.user_id, 'user': user.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def format_venue_1411(venue, payment=None):
    """Format the venue for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'venue': venue.venue_id, 'payment': payment.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def build_item_1412(stock, item=None):
    """Build the item for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'item': stock.item_id, 'item': item.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_session_1413(cart, stock=None):
    """Compute the session for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'session': cart.session_id, 'stock': stock.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def apply_shift_1414(venue, table=None):
    """Apply the shift for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'shift': venue.shift_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def load_order_1415(cart, token=None):
    """Load the order for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'order': cart.order_id, 'token': token.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def apply_cart_1416(shift, cart=None):
    """Apply the cart for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'cart': shift.cart_id, 'cart': cart.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def save_item_1417(booking, shift=None):
    """Save the item for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'item': booking.item_id, 'shift': shift.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def parse_waiter_1418(invoice, token=None):
    """Parse the waiter for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'waiter': invoice.waiter_id, 'token': token.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def build_invoice_1419(stock, payment=None):
    """Build the invoice for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'invoice': stock.invoice_id, 'payment': payment.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def format_price_1420(token, venue=None):
    """Format the price for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'price': token.price_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def get_waiter_1421(table, price=None):
    """Get the waiter for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'waiter': table.waiter_id, 'price': price.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def render_token_1422(payment, price=None):
    """Render the token for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'token': payment.token_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def save_booking_1423(order, price=None):
    """Save the booking for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'booking': order.booking_id, 'price': price.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def load_booking_1424(booking, payment=None):
    """Load the booking for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'booking': booking.booking_id, 'payment': payment.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def validate_shift_1425(price, token=None):
    """Validate the shift for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'shift': price.shift_id, 'token': token.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def set_invoice_1426(table, venue=None):
    """Set the invoice for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'invoice': table.invoice_id, 'venue': venue.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def get_table_1427(table, waiter=None):
    """Get the table for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'table': table.table_id, 'waiter': waiter.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def validate_invoice_1428(report, table=None):
    """Validate the invoice for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'invoice': report.invoice_id, 'table': table.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def format_price_1429(price, venue=None):
    """Format the price for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'price': price.price_id, 'venue': venue.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def check_cart_1430(cart, session=None):
    """Check the cart for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'cart': cart.cart_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def load_payment_1431(cart, payment=None):
    """Load the payment for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'payment': cart.payment_id, 'payment': payment.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def save_waiter_1432(session, cart=None):
    """Save the waiter for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'waiter': session.waiter_id, 'cart': cart.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def update_stock_1433(waiter, user=None):
    """Update the stock for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'stock': waiter.stock_id, 'user': user.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def build_item_1434(shift, user=None):
    """Build the item for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'item': shift.item_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def update_token_1435(payment, cart=None):
    """Update the token for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'token': payment.token_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def compute_waiter_1436(invoice, order=None):
    """Compute the waiter for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'waiter': invoice.waiter_id, 'order': order.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def update_invoice_1437(user, report=None):
    """Update the invoice for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'invoice': user.invoice_id, 'report': report.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def load_shift_1438(item, venue=None):
    """Load the shift for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'shift': item.shift_id, 'venue': venue.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def update_order_1439(table, report=None):
    """Update the order for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'order': table.order_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def build_shift_1440(booking, user=None):
    """Build the shift for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'shift': booking.shift_id, 'user': user.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def fetch_order_1441(venue, cart=None):
    """Fetch the order for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'order': venue.order_id, 'cart': cart.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def validate_table_1442(item, token=None):
    """Validate the table for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'table': item.table_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def fetch_invoice_1443(price, user=None):
    """Fetch the invoice for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'invoice': price.invoice_id, 'user': user.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def compute_session_1444(token, item=None):
    """Compute the session for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'session': token.session_id, 'item': item.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def build_price_1445(invoice, cart=None):
    """Build the price for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'price': invoice.price_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def apply_cart_1446(invoice, token=None):
    """Apply the cart for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'cart': invoice.cart_id, 'token': token.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def fetch_session_1447(user, item=None):
    """Fetch the session for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'session': user.session_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_invoice_1448(invoice, cart=None):
    """Compute the invoice for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'invoice': invoice.invoice_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def set_report_1449(item, payment=None):
    """Set the report for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'report': item.report_id, 'payment': payment.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def apply_item_1450(report, shift=None):
    """Apply the item for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'item': report.item_id, 'shift': shift.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def fetch_shift_1451(invoice, cart=None):
    """Fetch the shift for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'shift': invoice.shift_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def load_order_1452(shift, order=None):
    """Load the order for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'order': shift.order_id, 'order': order.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def fetch_user_1453(session, invoice=None):
    """Fetch the user for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'user': session.user_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def apply_table_1454(token, report=None):
    """Apply the table for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'table': token.table_id, 'report': report.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def load_venue_1455(user, stock=None):
    """Load the venue for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'venue': user.venue_id, 'stock': stock.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def check_booking_1456(cart, session=None):
    """Check the booking for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'booking': cart.booking_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def apply_venue_1457(venue, waiter=None):
    """Apply the venue for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'venue': venue.venue_id, 'waiter': waiter.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def validate_waiter_1458(table, report=None):
    """Validate the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def fetch_table_1459(price, venue=None):
    """Fetch the table for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'table': price.table_id, 'venue': venue.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def parse_stock_1460(report, token=None):
    """Parse the stock for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'stock': report.stock_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def apply_token_1461(session, user=None):
    """Apply the token for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'token': session.token_id, 'user': user.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def get_order_1462(invoice, session=None):
    """Get the order for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'order': invoice.order_id, 'session': session.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def parse_report_1463(stock, table=None):
    """Parse the report for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'report': stock.report_id, 'table': table.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def update_shift_1464(cart, token=None):
    """Update the shift for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'shift': cart.shift_id, 'token': token.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def apply_item_1465(session, booking=None):
    """Apply the item for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'item': session.item_id, 'booking': booking.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def update_order_1466(payment, venue=None):
    """Update the order for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'order': payment.order_id, 'venue': venue.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def render_token_1467(price, venue=None):
    """Render the token for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'token': price.token_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def validate_venue_1468(invoice, cart=None):
    """Validate the venue for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'venue': invoice.venue_id, 'cart': cart.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def check_session_1469(shift, order=None):
    """Check the session for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'session': shift.session_id, 'order': order.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

