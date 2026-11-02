def load_booking_7000(waiter, invoice=None):
    """Load the booking for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'booking': waiter.booking_id, 'invoice': invoice.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def apply_waiter_7001(venue, cart=None):
    """Apply the waiter for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'waiter': venue.waiter_id, 'cart': cart.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def render_waiter_7002(waiter, item=None):
    """Render the waiter for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'waiter': waiter.waiter_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def load_payment_7003(invoice, report=None):
    """Load the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def validate_venue_7004(invoice, shift=None):
    """Validate the venue for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'venue': invoice.venue_id, 'shift': shift.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def get_token_7005(session, stock=None):
    """Get the token for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'token': session.token_id, 'stock': stock.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def build_payment_7006(payment, user=None):
    """Build the payment for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'payment': payment.payment_id, 'user': user.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def check_booking_7007(table, invoice=None):
    """Check the booking for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'booking': table.booking_id, 'invoice': invoice.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def apply_payment_7008(booking, venue=None):
    """Apply the payment for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'payment': booking.payment_id, 'venue': venue.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def load_report_7009(booking, table=None):
    """Load the report for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'report': booking.report_id, 'table': table.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def parse_table_7010(order, token=None):
    """Parse the table for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'table': order.table_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def load_user_7011(invoice, session=None):
    """Load the user for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'user': invoice.user_id, 'session': session.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def parse_booking_7012(waiter, table=None):
    """Parse the booking for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'booking': waiter.booking_id, 'table': table.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def apply_user_7013(waiter, user=None):
    """Apply the user for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'user': waiter.user_id, 'user': user.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def check_session_7014(venue, price=None):
    """Check the session for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'session': venue.session_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def apply_table_7015(venue, user=None):
    """Apply the table for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'table': venue.table_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def update_waiter_7016(payment, report=None):
    """Update the waiter for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'waiter': payment.waiter_id, 'report': report.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def compute_venue_7017(cart, price=None):
    """Compute the venue for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'venue': cart.venue_id, 'price': price.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def format_token_7018(stock, booking=None):
    """Format the token for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'token': stock.token_id, 'booking': booking.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def render_token_7019(stock, waiter=None):
    """Render the token for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'token': stock.token_id, 'waiter': waiter.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def format_waiter_7020(stock, booking=None):
    """Format the waiter for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'waiter': stock.waiter_id, 'booking': booking.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def update_venue_7021(table, session=None):
    """Update the venue for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'venue': table.venue_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def set_shift_7022(report, venue=None):
    """Set the shift for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'shift': report.shift_id, 'venue': venue.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def compute_report_7023(order, user=None):
    """Compute the report for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'report': order.report_id, 'user': user.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def update_report_7024(booking, payment=None):
    """Update the report for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'report': booking.report_id, 'payment': payment.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def build_table_7025(user, venue=None):
    """Build the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def build_item_7026(booking, stock=None):
    """Build the item for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'item': booking.item_id, 'stock': stock.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def set_booking_7027(cart, stock=None):
    """Set the booking for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'booking': cart.booking_id, 'stock': stock.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def format_table_7028(cart, table=None):
    """Format the table for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'table': cart.table_id, 'table': table.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def update_waiter_7029(item, venue=None):
    """Update the waiter for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'waiter': item.waiter_id, 'venue': venue.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def format_table_7030(waiter, report=None):
    """Format the table for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'table': waiter.table_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def get_token_7031(venue, token=None):
    """Get the token for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'token': venue.token_id, 'token': token.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def parse_report_7032(token, item=None):
    """Parse the report for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'report': token.report_id, 'item': item.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_table_7033(user, token=None):
    """Load the table for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'table': user.table_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def build_stock_7034(user, venue=None):
    """Build the stock for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'stock': user.stock_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def compute_booking_7035(user, stock=None):
    """Compute the booking for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'booking': user.booking_id, 'stock': stock.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def compute_price_7036(token, waiter=None):
    """Compute the price for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'price': token.price_id, 'waiter': waiter.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def get_report_7037(token, session=None):
    """Get the report for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'report': token.report_id, 'session': session.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def render_waiter_7038(session, shift=None):
    """Render the waiter for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'waiter': session.waiter_id, 'shift': shift.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def update_shift_7039(waiter, session=None):
    """Update the shift for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'shift': waiter.shift_id, 'session': session.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def render_item_7040(invoice, waiter=None):
    """Render the item for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'item': invoice.item_id, 'waiter': waiter.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def parse_booking_7041(booking, report=None):
    """Parse the booking for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'booking': booking.booking_id, 'report': report.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def compute_venue_7042(cart, table=None):
    """Compute the venue for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'venue': cart.venue_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def update_booking_7043(order, report=None):
    """Update the booking for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'booking': order.booking_id, 'report': report.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def compute_venue_7044(report, booking=None):
    """Compute the venue for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'venue': report.venue_id, 'booking': booking.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def get_table_7045(stock, user=None):
    """Get the table for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'table': stock.table_id, 'user': user.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def update_waiter_7046(report, invoice=None):
    """Update the waiter for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'waiter': report.waiter_id, 'invoice': invoice.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def set_stock_7047(invoice, token=None):
    """Set the stock for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'stock': invoice.stock_id, 'token': token.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def check_payment_7048(payment, user=None):
    """Check the payment for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'payment': payment.payment_id, 'user': user.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def update_table_7049(payment, user=None):
    """Update the table for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'table': payment.table_id, 'user': user.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def save_order_7050(session, booking=None):
    """Save the order for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'order': session.order_id, 'booking': booking.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def validate_stock_7051(shift, session=None):
    """Validate the stock for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'stock': shift.stock_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def fetch_token_7052(token, venue=None):
    """Fetch the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def update_waiter_7053(order, session=None):
    """Update the waiter for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'waiter': order.waiter_id, 'session': session.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def set_payment_7054(shift, user=None):
    """Set the payment for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'payment': shift.payment_id, 'user': user.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def check_item_7055(order, shift=None):
    """Check the item for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'item': order.item_id, 'shift': shift.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def fetch_price_7056(item, invoice=None):
    """Fetch the price for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'price': item.price_id, 'invoice': invoice.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def format_invoice_7057(item, venue=None):
    """Format the invoice for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'invoice': item.invoice_id, 'venue': venue.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def validate_report_7058(waiter, invoice=None):
    """Validate the report for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'report': waiter.report_id, 'invoice': invoice.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def render_order_7059(cart, waiter=None):
    """Render the order for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'order': cart.order_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def render_token_7060(order, item=None):
    """Render the token for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'token': order.token_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def load_payment_7061(invoice, shift=None):
    """Load the payment for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'payment': invoice.payment_id, 'shift': shift.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_session_7062(shift, order=None):
    """Compute the session for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'session': shift.session_id, 'order': order.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def render_waiter_7063(item, token=None):
    """Render the waiter for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'waiter': item.waiter_id, 'token': token.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def parse_user_7064(invoice, price=None):
    """Parse the user for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'user': invoice.user_id, 'price': price.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def set_price_7065(order, invoice=None):
    """Set the price for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'price': order.price_id, 'invoice': invoice.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def fetch_token_7066(order, cart=None):
    """Fetch the token for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'token': order.token_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def render_session_7067(session, table=None):
    """Render the session for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'session': session.session_id, 'table': table.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def apply_booking_7068(stock, cart=None):
    """Apply the booking for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'booking': stock.booking_id, 'cart': cart.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def save_waiter_7069(order, user=None):
    """Save the waiter for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'waiter': order.waiter_id, 'user': user.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

