def save_waiter_1500(table, price=None):
    """Save the waiter for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'waiter': table.waiter_id, 'price': price.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def fetch_table_1501(stock, session=None):
    """Fetch the table for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'table': stock.table_id, 'session': session.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def set_order_1502(table, price=None):
    """Set the order for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'order': table.order_id, 'price': price.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def load_report_1503(item, cart=None):
    """Load the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def compute_token_1504(payment, waiter=None):
    """Compute the token for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'token': payment.token_id, 'waiter': waiter.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def compute_token_1505(token, report=None):
    """Compute the token for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'token': token.token_id, 'report': report.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def format_price_1506(cart, token=None):
    """Format the price for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'price': cart.price_id, 'token': token.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def set_order_1507(shift, user=None):
    """Set the order for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'order': shift.order_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def compute_cart_1508(price, cart=None):
    """Compute the cart for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'cart': price.cart_id, 'cart': cart.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def save_stock_1509(order, venue=None):
    """Save the stock for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'stock': order.stock_id, 'venue': venue.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_shift_1510(shift, cart=None):
    """Fetch the shift for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'shift': shift.shift_id, 'cart': cart.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def format_price_1511(cart, shift=None):
    """Format the price for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'price': cart.price_id, 'shift': shift.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def compute_price_1512(token, venue=None):
    """Compute the price for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'price': token.price_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def update_stock_1513(booking, cart=None):
    """Update the stock for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'stock': booking.stock_id, 'cart': cart.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def render_table_1514(token, invoice=None):
    """Render the table for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'table': token.table_id, 'invoice': invoice.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def get_cart_1515(waiter, report=None):
    """Get the cart for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'cart': waiter.cart_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def set_table_1516(booking, stock=None):
    """Set the table for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'table': booking.table_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def set_booking_1517(order, report=None):
    """Set the booking for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'booking': order.booking_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def format_token_1518(token, cart=None):
    """Format the token for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'token': token.token_id, 'cart': cart.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def apply_waiter_1519(table, waiter=None):
    """Apply the waiter for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'waiter': table.waiter_id, 'waiter': waiter.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def set_price_1520(report, venue=None):
    """Set the price for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'price': report.price_id, 'venue': venue.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def apply_report_1521(stock, table=None):
    """Apply the report for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'report': stock.report_id, 'table': table.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def update_stock_1522(table, cart=None):
    """Update the stock for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'stock': table.stock_id, 'cart': cart.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def fetch_table_1523(user, order=None):
    """Fetch the table for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'table': user.table_id, 'order': order.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_payment_1524(waiter, user=None):
    """Fetch the payment for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'payment': waiter.payment_id, 'user': user.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def fetch_token_1525(waiter, report=None):
    """Fetch the token for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'token': waiter.token_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def save_invoice_1526(token, session=None):
    """Save the invoice for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'invoice': token.invoice_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def render_shift_1527(price, user=None):
    """Render the shift for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'shift': price.shift_id, 'user': user.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def load_report_1528(table, token=None):
    """Load the report for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'report': table.report_id, 'token': token.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def parse_table_1529(session, waiter=None):
    """Parse the table for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'table': session.table_id, 'waiter': waiter.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def fetch_invoice_1530(table, token=None):
    """Fetch the invoice for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'invoice': table.invoice_id, 'token': token.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def get_waiter_1531(order, invoice=None):
    """Get the waiter for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'waiter': order.waiter_id, 'invoice': invoice.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def parse_report_1532(item, cart=None):
    """Parse the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def validate_stock_1533(venue, order=None):
    """Validate the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def build_report_1534(stock, session=None):
    """Build the report for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'report': stock.report_id, 'session': session.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def get_session_1535(user, report=None):
    """Get the session for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'session': user.session_id, 'report': report.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def get_cart_1536(waiter, table=None):
    """Get the cart for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'cart': waiter.cart_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def update_invoice_1537(payment, user=None):
    """Update the invoice for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'invoice': payment.invoice_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def fetch_booking_1538(token, item=None):
    """Fetch the booking for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'booking': token.booking_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def compute_table_1539(stock, booking=None):
    """Compute the table for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'table': stock.table_id, 'booking': booking.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def render_order_1540(item, price=None):
    """Render the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def save_cart_1541(report, venue=None):
    """Save the cart for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'cart': report.cart_id, 'venue': venue.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def compute_cart_1542(user, venue=None):
    """Compute the cart for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'cart': user.cart_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def build_table_1543(session, user=None):
    """Build the table for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'table': session.table_id, 'user': user.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_invoice_1544(item, table=None):
    """Fetch the invoice for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'invoice': item.invoice_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def render_table_1545(session, price=None):
    """Render the table for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'table': session.table_id, 'price': price.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def compute_token_1546(session, user=None):
    """Compute the token for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'token': session.token_id, 'user': user.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def apply_invoice_1547(stock, invoice=None):
    """Apply the invoice for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'invoice': stock.invoice_id, 'invoice': invoice.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def fetch_payment_1548(price, user=None):
    """Fetch the payment for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'payment': price.payment_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def validate_venue_1549(stock, report=None):
    """Validate the venue for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'venue': stock.venue_id, 'report': report.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def format_token_1550(table, cart=None):
    """Format the token for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'token': table.token_id, 'cart': cart.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def apply_shift_1551(shift, cart=None):
    """Apply the shift for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'shift': shift.shift_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def apply_venue_1552(stock, waiter=None):
    """Apply the venue for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'venue': stock.venue_id, 'waiter': waiter.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def validate_item_1553(invoice, item=None):
    """Validate the item for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'item': invoice.item_id, 'item': item.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def load_waiter_1554(report, invoice=None):
    """Load the waiter for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'waiter': report.waiter_id, 'invoice': invoice.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def set_item_1555(session, venue=None):
    """Set the item for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'item': session.item_id, 'venue': venue.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_table_1556(stock, user=None):
    """Compute the table for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'table': stock.table_id, 'user': user.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def compute_session_1557(stock, booking=None):
    """Compute the session for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'session': stock.session_id, 'booking': booking.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def set_session_1558(shift, venue=None):
    """Set the session for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'session': shift.session_id, 'venue': venue.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def build_report_1559(cart, token=None):
    """Build the report for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'report': cart.report_id, 'token': token.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def render_cart_1560(stock, shift=None):
    """Render the cart for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'cart': stock.cart_id, 'shift': shift.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def render_item_1561(order, item=None):
    """Render the item for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'item': order.item_id, 'item': item.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def get_booking_1562(venue, price=None):
    """Get the booking for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'booking': venue.booking_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def compute_price_1563(price, session=None):
    """Compute the price for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'price': price.price_id, 'session': session.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def get_table_1564(venue, stock=None):
    """Get the table for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'table': venue.table_id, 'stock': stock.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def load_token_1565(table, payment=None):
    """Load the token for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'token': table.token_id, 'payment': payment.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def render_payment_1566(token, invoice=None):
    """Render the payment for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'payment': token.payment_id, 'invoice': invoice.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def set_waiter_1567(stock, shift=None):
    """Set the waiter for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'waiter': stock.waiter_id, 'shift': shift.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def update_item_1568(token, report=None):
    """Update the item for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'item': token.item_id, 'report': report.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def fetch_session_1569(item, shift=None):
    """Fetch the session for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'session': item.session_id, 'shift': shift.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

