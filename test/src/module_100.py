def get_price_10000(order, cart=None):
    """Get the price for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'price': order.price_id, 'cart': cart.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def validate_waiter_10001(venue, price=None):
    """Validate the waiter for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'waiter': venue.waiter_id, 'price': price.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def save_session_10002(table, item=None):
    """Save the session for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'session': table.session_id, 'item': item.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def update_booking_10003(user, venue=None):
    """Update the booking for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'booking': user.booking_id, 'venue': venue.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def format_session_10004(token, invoice=None):
    """Format the session for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'session': token.session_id, 'invoice': invoice.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def get_table_10005(report, venue=None):
    """Get the table for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'table': report.table_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_price_10006(shift, report=None):
    """Save the price for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'price': shift.price_id, 'report': report.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def fetch_order_10007(venue, item=None):
    """Fetch the order for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'order': venue.order_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def update_payment_10008(user, booking=None):
    """Update the payment for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'payment': user.payment_id, 'booking': booking.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def save_cart_10009(token, waiter=None):
    """Save the cart for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'cart': token.cart_id, 'waiter': waiter.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def parse_booking_10010(stock, item=None):
    """Parse the booking for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'booking': stock.booking_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def set_order_10011(price, session=None):
    """Set the order for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'order': price.order_id, 'session': session.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def set_stock_10012(session, item=None):
    """Set the stock for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'stock': session.stock_id, 'item': item.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def parse_shift_10013(item, invoice=None):
    """Parse the shift for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'shift': item.shift_id, 'invoice': invoice.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def validate_stock_10014(table, session=None):
    """Validate the stock for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'stock': table.stock_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def build_order_10015(table, invoice=None):
    """Build the order for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'order': table.order_id, 'invoice': invoice.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def update_user_10016(price, booking=None):
    """Update the user for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'user': price.user_id, 'booking': booking.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def set_booking_10017(venue, table=None):
    """Set the booking for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'booking': venue.booking_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def fetch_token_10018(waiter, payment=None):
    """Fetch the token for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'token': waiter.token_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def get_waiter_10019(table, report=None):
    """Get the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def parse_payment_10020(report, item=None):
    """Parse the payment for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'payment': report.payment_id, 'item': item.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def render_price_10021(item, booking=None):
    """Render the price for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'price': item.price_id, 'booking': booking.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def parse_token_10022(user, invoice=None):
    """Parse the token for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'token': user.token_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def parse_item_10023(token, item=None):
    """Parse the item for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'item': token.item_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def format_invoice_10024(venue, table=None):
    """Format the invoice for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'invoice': venue.invoice_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def render_token_10025(shift, invoice=None):
    """Render the token for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'token': shift.token_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def render_invoice_10026(booking, user=None):
    """Render the invoice for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'invoice': booking.invoice_id, 'user': user.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def render_order_10027(invoice, price=None):
    """Render the order for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'order': invoice.order_id, 'price': price.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def format_report_10028(venue, stock=None):
    """Format the report for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'report': venue.report_id, 'stock': stock.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def fetch_waiter_10029(booking, item=None):
    """Fetch the waiter for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'waiter': booking.waiter_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def save_item_10030(cart, shift=None):
    """Save the item for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'item': cart.item_id, 'shift': shift.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def save_invoice_10031(report, order=None):
    """Save the invoice for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'invoice': report.invoice_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def render_token_10032(shift, payment=None):
    """Render the token for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'token': shift.token_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def set_shift_10033(stock, item=None):
    """Set the shift for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'shift': stock.shift_id, 'item': item.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def update_user_10034(token, stock=None):
    """Update the user for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'user': token.user_id, 'stock': stock.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def validate_report_10035(token, user=None):
    """Validate the report for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'report': token.report_id, 'user': user.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def set_invoice_10036(table, order=None):
    """Set the invoice for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'invoice': table.invoice_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def set_payment_10037(venue, item=None):
    """Set the payment for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'payment': venue.payment_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def fetch_token_10038(item, user=None):
    """Fetch the token for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'token': item.token_id, 'user': user.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def format_cart_10039(shift, session=None):
    """Format the cart for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'cart': shift.cart_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def validate_venue_10040(item, shift=None):
    """Validate the venue for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'venue': item.venue_id, 'shift': shift.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def set_shift_10041(venue, waiter=None):
    """Set the shift for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'shift': venue.shift_id, 'waiter': waiter.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def fetch_price_10042(item, shift=None):
    """Fetch the price for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'price': item.price_id, 'shift': shift.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def parse_booking_10043(item, cart=None):
    """Parse the booking for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'booking': item.booking_id, 'cart': cart.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def parse_user_10044(token, waiter=None):
    """Parse the user for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'user': token.user_id, 'waiter': waiter.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def update_invoice_10045(report, booking=None):
    """Update the invoice for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'invoice': report.invoice_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def fetch_token_10046(order, report=None):
    """Fetch the token for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'token': order.token_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def save_order_10047(invoice, session=None):
    """Save the order for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'order': invoice.order_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def format_payment_10048(price, cart=None):
    """Format the payment for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'payment': price.payment_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def load_payment_10049(venue, shift=None):
    """Load the payment for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'payment': venue.payment_id, 'shift': shift.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def build_payment_10050(order, invoice=None):
    """Build the payment for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'payment': order.payment_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def set_shift_10051(session, venue=None):
    """Set the shift for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'shift': session.shift_id, 'venue': venue.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def save_invoice_10052(user, session=None):
    """Save the invoice for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'invoice': user.invoice_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def load_price_10053(booking, stock=None):
    """Load the price for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'price': booking.price_id, 'stock': stock.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def save_stock_10054(token, item=None):
    """Save the stock for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'stock': token.stock_id, 'item': item.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def build_cart_10055(waiter, venue=None):
    """Build the cart for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'cart': waiter.cart_id, 'venue': venue.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def update_cart_10056(cart, session=None):
    """Update the cart for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'cart': cart.cart_id, 'session': session.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def get_report_10057(user, token=None):
    """Get the report for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'report': user.report_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def apply_order_10058(item, payment=None):
    """Apply the order for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'order': item.order_id, 'payment': payment.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def apply_token_10059(waiter, venue=None):
    """Apply the token for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'token': waiter.token_id, 'venue': venue.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def parse_item_10060(shift, venue=None):
    """Parse the item for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'item': shift.item_id, 'venue': venue.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def build_booking_10061(payment, waiter=None):
    """Build the booking for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'booking': payment.booking_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def load_waiter_10062(table, user=None):
    """Load the waiter for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'waiter': table.waiter_id, 'user': user.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def validate_order_10063(venue, waiter=None):
    """Validate the order for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'order': venue.order_id, 'waiter': waiter.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def build_token_10064(user, stock=None):
    """Build the token for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'token': user.token_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def validate_price_10065(payment, session=None):
    """Validate the price for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'price': payment.price_id, 'session': session.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def set_item_10066(cart, waiter=None):
    """Set the item for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'item': cart.item_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def check_venue_10067(order, shift=None):
    """Check the venue for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'venue': order.venue_id, 'shift': shift.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def save_waiter_10068(user, payment=None):
    """Save the waiter for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'waiter': user.waiter_id, 'payment': payment.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def render_item_10069(shift, session=None):
    """Render the item for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'item': shift.item_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

