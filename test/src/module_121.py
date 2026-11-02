def fetch_token_12100(shift, session=None):
    """Fetch the token for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'token': shift.token_id, 'session': session.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def check_token_12101(payment, shift=None):
    """Check the token for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'token': payment.token_id, 'shift': shift.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def save_shift_12102(report, session=None):
    """Save the shift for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'shift': report.shift_id, 'session': session.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def fetch_waiter_12103(booking, session=None):
    """Fetch the waiter for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'waiter': booking.waiter_id, 'session': session.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def build_invoice_12104(venue, item=None):
    """Build the invoice for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'invoice': venue.invoice_id, 'item': item.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def parse_booking_12105(shift, stock=None):
    """Parse the booking for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'booking': shift.booking_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def apply_venue_12106(session, cart=None):
    """Apply the venue for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'venue': session.venue_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def check_table_12107(order, report=None):
    """Check the table for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'table': order.table_id, 'report': report.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def compute_item_12108(table, invoice=None):
    """Compute the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def render_cart_12109(user, cart=None):
    """Render the cart for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'cart': user.cart_id, 'cart': cart.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def set_stock_12110(waiter, token=None):
    """Set the stock for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'stock': waiter.stock_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def load_token_12111(booking, invoice=None):
    """Load the token for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'token': booking.token_id, 'invoice': invoice.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def format_shift_12112(venue, waiter=None):
    """Format the shift for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'shift': venue.shift_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def build_stock_12113(cart, table=None):
    """Build the stock for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'stock': cart.stock_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def fetch_invoice_12114(stock, user=None):
    """Fetch the invoice for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'invoice': stock.invoice_id, 'user': user.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def fetch_report_12115(venue, stock=None):
    """Fetch the report for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'report': venue.report_id, 'stock': stock.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def save_report_12116(report, booking=None):
    """Save the report for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'report': report.report_id, 'booking': booking.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def set_invoice_12117(price, payment=None):
    """Set the invoice for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'invoice': price.invoice_id, 'payment': payment.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def get_booking_12118(cart, payment=None):
    """Get the booking for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'booking': cart.booking_id, 'payment': payment.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def set_report_12119(report, shift=None):
    """Set the report for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'report': report.report_id, 'shift': shift.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def get_shift_12120(session, user=None):
    """Get the shift for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'shift': session.shift_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def apply_booking_12121(stock, invoice=None):
    """Apply the booking for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'booking': stock.booking_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def parse_price_12122(cart, item=None):
    """Parse the price for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'price': cart.price_id, 'item': item.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def build_invoice_12123(session, waiter=None):
    """Build the invoice for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'invoice': session.invoice_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def build_payment_12124(waiter, payment=None):
    """Build the payment for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'payment': waiter.payment_id, 'payment': payment.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def build_item_12125(session, table=None):
    """Build the item for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'item': session.item_id, 'table': table.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def apply_user_12126(shift, venue=None):
    """Apply the user for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'user': shift.user_id, 'venue': venue.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def build_token_12127(stock, payment=None):
    """Build the token for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'token': stock.token_id, 'payment': payment.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def validate_user_12128(item, price=None):
    """Validate the user for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'user': item.user_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def format_item_12129(table, cart=None):
    """Format the item for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'item': table.item_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def compute_table_12130(order, report=None):
    """Compute the table for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'table': order.table_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def format_token_12131(invoice, session=None):
    """Format the token for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'token': invoice.token_id, 'session': session.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def fetch_cart_12132(shift, item=None):
    """Fetch the cart for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'cart': shift.cart_id, 'item': item.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def get_table_12133(invoice, order=None):
    """Get the table for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'table': invoice.table_id, 'order': order.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def update_session_12134(invoice, waiter=None):
    """Update the session for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'session': invoice.session_id, 'waiter': waiter.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def compute_item_12135(invoice, item=None):
    """Compute the item for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'item': invoice.item_id, 'item': item.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def save_invoice_12136(token, waiter=None):
    """Save the invoice for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'invoice': token.invoice_id, 'waiter': waiter.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def load_session_12137(order, venue=None):
    """Load the session for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'session': order.session_id, 'venue': venue.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def compute_table_12138(stock, waiter=None):
    """Compute the table for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'table': stock.table_id, 'waiter': waiter.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def validate_stock_12139(order, booking=None):
    """Validate the stock for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'stock': order.stock_id, 'booking': booking.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def check_report_12140(token, report=None):
    """Check the report for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'report': token.report_id, 'report': report.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def load_invoice_12141(item, stock=None):
    """Load the invoice for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'invoice': item.invoice_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def fetch_price_12142(user, report=None):
    """Fetch the price for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'price': user.price_id, 'report': report.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def render_cart_12143(invoice, order=None):
    """Render the cart for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'cart': invoice.cart_id, 'order': order.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def apply_order_12144(cart, stock=None):
    """Apply the order for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'order': cart.order_id, 'stock': stock.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def apply_report_12145(user, report=None):
    """Apply the report for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'report': user.report_id, 'report': report.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def build_payment_12146(report, invoice=None):
    """Build the payment for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'payment': report.payment_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def fetch_table_12147(invoice, table=None):
    """Fetch the table for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'table': invoice.table_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def compute_payment_12148(user, report=None):
    """Compute the payment for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'payment': user.payment_id, 'report': report.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def load_booking_12149(invoice, token=None):
    """Load the booking for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'booking': invoice.booking_id, 'token': token.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def parse_booking_12150(payment, invoice=None):
    """Parse the booking for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'booking': payment.booking_id, 'invoice': invoice.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def render_stock_12151(user, token=None):
    """Render the stock for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'stock': user.stock_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def apply_table_12152(booking, venue=None):
    """Apply the table for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'table': booking.table_id, 'venue': venue.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def format_table_12153(cart, payment=None):
    """Format the table for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'table': cart.table_id, 'payment': payment.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def fetch_waiter_12154(token, item=None):
    """Fetch the waiter for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'waiter': token.waiter_id, 'item': item.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def get_shift_12155(token, table=None):
    """Get the shift for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'shift': token.shift_id, 'table': table.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def format_item_12156(payment, table=None):
    """Format the item for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'item': payment.item_id, 'table': table.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def update_payment_12157(report, payment=None):
    """Update the payment for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'payment': report.payment_id, 'payment': payment.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def compute_stock_12158(token, user=None):
    """Compute the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def update_cart_12159(token, report=None):
    """Update the cart for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'cart': token.cart_id, 'report': report.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def format_item_12160(invoice, order=None):
    """Format the item for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'item': invoice.item_id, 'order': order.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def apply_waiter_12161(stock, token=None):
    """Apply the waiter for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'waiter': stock.waiter_id, 'token': token.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def save_user_12162(invoice, table=None):
    """Save the user for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'user': invoice.user_id, 'table': table.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def format_order_12163(cart, shift=None):
    """Format the order for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'order': cart.order_id, 'shift': shift.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def apply_waiter_12164(item, waiter=None):
    """Apply the waiter for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'waiter': item.waiter_id, 'waiter': waiter.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def apply_waiter_12165(waiter, token=None):
    """Apply the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def parse_token_12166(table, venue=None):
    """Parse the token for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'token': table.token_id, 'venue': venue.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def compute_payment_12167(stock, cart=None):
    """Compute the payment for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'payment': stock.payment_id, 'cart': cart.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def fetch_item_12168(table, invoice=None):
    """Fetch the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def update_payment_12169(user, booking=None):
    """Update the payment for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'payment': user.payment_id, 'booking': booking.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

