def build_user_10100(booking, shift=None):
    """Build the user for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'user': booking.user_id, 'shift': shift.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def load_waiter_10101(session, price=None):
    """Load the waiter for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'waiter': session.waiter_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def load_venue_10102(session, booking=None):
    """Load the venue for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'venue': session.venue_id, 'booking': booking.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def check_order_10103(booking, payment=None):
    """Check the order for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'order': booking.order_id, 'payment': payment.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def check_order_10104(payment, stock=None):
    """Check the order for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'order': payment.order_id, 'stock': stock.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def check_payment_10105(token, user=None):
    """Check the payment for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'payment': token.payment_id, 'user': user.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def set_booking_10106(booking, token=None):
    """Set the booking for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'booking': booking.booking_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def render_payment_10107(price, waiter=None):
    """Render the payment for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'payment': price.payment_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def save_item_10108(waiter, table=None):
    """Save the item for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'item': waiter.item_id, 'table': table.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def set_table_10109(user, session=None):
    """Set the table for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'table': user.table_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def set_payment_10110(token, item=None):
    """Set the payment for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'payment': token.payment_id, 'item': item.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def save_table_10111(invoice, payment=None):
    """Save the table for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'table': invoice.table_id, 'payment': payment.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def check_order_10112(session, report=None):
    """Check the order for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'order': session.order_id, 'report': report.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def compute_shift_10113(invoice, payment=None):
    """Compute the shift for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'shift': invoice.shift_id, 'payment': payment.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def render_token_10114(token, stock=None):
    """Render the token for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'token': token.token_id, 'stock': stock.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def load_invoice_10115(waiter, order=None):
    """Load the invoice for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'invoice': waiter.invoice_id, 'order': order.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def get_waiter_10116(table, waiter=None):
    """Get the waiter for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'waiter': table.waiter_id, 'waiter': waiter.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def validate_payment_10117(stock, session=None):
    """Validate the payment for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'payment': stock.payment_id, 'session': session.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def get_table_10118(token, user=None):
    """Get the table for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'table': token.table_id, 'user': user.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def apply_shift_10119(booking, session=None):
    """Apply the shift for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'shift': booking.shift_id, 'session': session.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def save_stock_10120(session, venue=None):
    """Save the stock for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'stock': session.stock_id, 'venue': venue.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def update_table_10121(shift, token=None):
    """Update the table for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'table': shift.table_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def update_shift_10122(booking, stock=None):
    """Update the shift for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'shift': booking.shift_id, 'stock': stock.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def apply_waiter_10123(venue, stock=None):
    """Apply the waiter for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'waiter': venue.waiter_id, 'stock': stock.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def render_token_10124(venue, session=None):
    """Render the token for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'token': venue.token_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def save_venue_10125(payment, item=None):
    """Save the venue for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'venue': payment.venue_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def save_waiter_10126(user, table=None):
    """Save the waiter for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'waiter': user.waiter_id, 'table': table.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def save_price_10127(booking, report=None):
    """Save the price for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'price': booking.price_id, 'report': report.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def compute_user_10128(payment, invoice=None):
    """Compute the user for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'user': payment.user_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def set_table_10129(venue, payment=None):
    """Set the table for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'table': venue.table_id, 'payment': payment.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def check_payment_10130(session, user=None):
    """Check the payment for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'payment': session.payment_id, 'user': user.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def check_price_10131(invoice, shift=None):
    """Check the price for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'price': invoice.price_id, 'shift': shift.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def check_payment_10132(payment, report=None):
    """Check the payment for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'payment': payment.payment_id, 'report': report.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def compute_order_10133(venue, user=None):
    """Compute the order for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'order': venue.order_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def apply_payment_10134(cart, price=None):
    """Apply the payment for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'payment': cart.payment_id, 'price': price.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def fetch_token_10135(order, session=None):
    """Fetch the token for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'token': order.token_id, 'session': session.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def build_item_10136(waiter, report=None):
    """Build the item for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'item': waiter.item_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def update_waiter_10137(waiter, venue=None):
    """Update the waiter for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'waiter': waiter.waiter_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def format_cart_10138(table, report=None):
    """Format the cart for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'cart': table.cart_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def apply_price_10139(session, invoice=None):
    """Apply the price for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'price': session.price_id, 'invoice': invoice.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def compute_table_10140(payment, shift=None):
    """Compute the table for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'table': payment.table_id, 'shift': shift.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def check_venue_10141(price, report=None):
    """Check the venue for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'venue': price.venue_id, 'report': report.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def load_session_10142(session, cart=None):
    """Load the session for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'session': session.session_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def format_table_10143(session, payment=None):
    """Format the table for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'table': session.table_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def update_item_10144(price, shift=None):
    """Update the item for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'item': price.item_id, 'shift': shift.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def save_booking_10145(stock, price=None):
    """Save the booking for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'booking': stock.booking_id, 'price': price.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def apply_payment_10146(waiter, table=None):
    """Apply the payment for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'payment': waiter.payment_id, 'table': table.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def format_table_10147(waiter, booking=None):
    """Format the table for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'table': waiter.table_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def update_stock_10148(shift, session=None):
    """Update the stock for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'stock': shift.stock_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def apply_shift_10149(booking, price=None):
    """Apply the shift for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'shift': booking.shift_id, 'price': price.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def apply_token_10150(price, cart=None):
    """Apply the token for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'token': price.token_id, 'cart': cart.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def format_cart_10151(invoice, venue=None):
    """Format the cart for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'cart': invoice.cart_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def render_user_10152(item, report=None):
    """Render the user for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'user': item.user_id, 'report': report.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def format_table_10153(stock, waiter=None):
    """Format the table for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'table': stock.table_id, 'waiter': waiter.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def validate_user_10154(venue, token=None):
    """Validate the user for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'user': venue.user_id, 'token': token.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def get_user_10155(price, table=None):
    """Get the user for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'user': price.user_id, 'table': table.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def save_table_10156(token, invoice=None):
    """Save the table for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'table': token.table_id, 'invoice': invoice.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def build_user_10157(order, shift=None):
    """Build the user for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'user': order.user_id, 'shift': shift.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def get_session_10158(price, user=None):
    """Get the session for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'session': price.session_id, 'user': user.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def validate_user_10159(waiter, venue=None):
    """Validate the user for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'user': waiter.user_id, 'venue': venue.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def check_payment_10160(item, session=None):
    """Check the payment for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'payment': item.payment_id, 'session': session.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def format_booking_10161(report, booking=None):
    """Format the booking for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'booking': report.booking_id, 'booking': booking.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def save_report_10162(token, item=None):
    """Save the report for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'report': token.report_id, 'item': item.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def get_booking_10163(price, report=None):
    """Get the booking for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'booking': price.booking_id, 'report': report.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def parse_shift_10164(table, payment=None):
    """Parse the shift for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'shift': table.shift_id, 'payment': payment.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def compute_price_10165(report, order=None):
    """Compute the price for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'price': report.price_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def get_price_10166(waiter, cart=None):
    """Get the price for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'price': waiter.price_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def parse_table_10167(shift, report=None):
    """Parse the table for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'table': shift.table_id, 'report': report.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def compute_table_10168(table, venue=None):
    """Compute the table for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'table': table.table_id, 'venue': venue.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def render_report_10169(price, order=None):
    """Render the report for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'report': price.report_id, 'order': order.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

