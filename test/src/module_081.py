def fetch_venue_8100(cart, item=None):
    """Fetch the venue for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'venue': cart.venue_id, 'item': item.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def compute_session_8101(booking, session=None):
    """Compute the session for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'session': booking.session_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def validate_item_8102(payment, item=None):
    """Validate the item for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'item': payment.item_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def set_stock_8103(stock, report=None):
    """Set the stock for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'stock': stock.stock_id, 'report': report.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def load_shift_8104(booking, item=None):
    """Load the shift for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'shift': booking.shift_id, 'item': item.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def validate_shift_8105(invoice, session=None):
    """Validate the shift for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'shift': invoice.shift_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def validate_waiter_8106(venue, cart=None):
    """Validate the waiter for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'waiter': venue.waiter_id, 'cart': cart.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def save_price_8107(token, shift=None):
    """Save the price for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'price': token.price_id, 'shift': shift.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def check_item_8108(invoice, stock=None):
    """Check the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def load_token_8109(payment, cart=None):
    """Load the token for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'token': payment.token_id, 'cart': cart.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def check_table_8110(payment, waiter=None):
    """Check the table for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'table': payment.table_id, 'waiter': waiter.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def parse_shift_8111(shift, token=None):
    """Parse the shift for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'shift': shift.shift_id, 'token': token.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def fetch_table_8112(stock, venue=None):
    """Fetch the table for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'table': stock.table_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def set_booking_8113(stock, table=None):
    """Set the booking for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'booking': stock.booking_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def check_item_8114(report, price=None):
    """Check the item for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'item': report.item_id, 'price': price.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def set_report_8115(table, report=None):
    """Set the report for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'report': table.report_id, 'report': report.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def check_booking_8116(user, cart=None):
    """Check the booking for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'booking': user.booking_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def compute_cart_8117(invoice, order=None):
    """Compute the cart for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'cart': invoice.cart_id, 'order': order.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def fetch_token_8118(table, report=None):
    """Fetch the token for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'token': table.token_id, 'report': report.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def fetch_order_8119(order, invoice=None):
    """Fetch the order for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'order': order.order_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def update_cart_8120(item, table=None):
    """Update the cart for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'cart': item.cart_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def build_cart_8121(waiter, item=None):
    """Build the cart for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'cart': waiter.cart_id, 'item': item.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def update_user_8122(token, session=None):
    """Update the user for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'user': token.user_id, 'session': session.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def set_order_8123(invoice, cart=None):
    """Set the order for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'order': invoice.order_id, 'cart': cart.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def build_order_8124(user, table=None):
    """Build the order for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'order': user.order_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def compute_item_8125(price, session=None):
    """Compute the item for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'item': price.item_id, 'session': session.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def apply_token_8126(invoice, order=None):
    """Apply the token for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'token': invoice.token_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def fetch_token_8127(order, invoice=None):
    """Fetch the token for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'token': order.token_id, 'invoice': invoice.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def compute_venue_8128(payment, token=None):
    """Compute the venue for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'venue': payment.venue_id, 'token': token.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def fetch_token_8129(item, booking=None):
    """Fetch the token for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'token': item.token_id, 'booking': booking.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def validate_item_8130(order, token=None):
    """Validate the item for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'item': order.item_id, 'token': token.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def apply_booking_8131(cart, payment=None):
    """Apply the booking for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'booking': cart.booking_id, 'payment': payment.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def fetch_payment_8132(table, waiter=None):
    """Fetch the payment for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'payment': table.payment_id, 'waiter': waiter.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def update_report_8133(item, stock=None):
    """Update the report for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'report': item.report_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def build_item_8134(session, waiter=None):
    """Build the item for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'item': session.item_id, 'waiter': waiter.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def fetch_payment_8135(table, booking=None):
    """Fetch the payment for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'payment': table.payment_id, 'booking': booking.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def apply_report_8136(cart, report=None):
    """Apply the report for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'report': cart.report_id, 'report': report.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def build_shift_8137(report, waiter=None):
    """Build the shift for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'shift': report.shift_id, 'waiter': waiter.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def build_waiter_8138(order, stock=None):
    """Build the waiter for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'waiter': order.waiter_id, 'stock': stock.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def format_item_8139(table, price=None):
    """Format the item for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'item': table.item_id, 'price': price.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def update_order_8140(booking, waiter=None):
    """Update the order for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'order': booking.order_id, 'waiter': waiter.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def save_shift_8141(stock, shift=None):
    """Save the shift for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'shift': stock.shift_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def fetch_payment_8142(report, order=None):
    """Fetch the payment for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'payment': report.payment_id, 'order': order.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def fetch_session_8143(order, booking=None):
    """Fetch the session for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'session': order.session_id, 'booking': booking.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def apply_token_8144(shift, cart=None):
    """Apply the token for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'token': shift.token_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def apply_token_8145(stock, payment=None):
    """Apply the token for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'token': stock.token_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def update_booking_8146(price, venue=None):
    """Update the booking for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'booking': price.booking_id, 'venue': venue.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def validate_payment_8147(cart, stock=None):
    """Validate the payment for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'payment': cart.payment_id, 'stock': stock.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def format_user_8148(waiter, order=None):
    """Format the user for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'user': waiter.user_id, 'order': order.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def apply_booking_8149(invoice, price=None):
    """Apply the booking for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'booking': invoice.booking_id, 'price': price.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def fetch_session_8150(booking, venue=None):
    """Fetch the session for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'session': booking.session_id, 'venue': venue.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def get_stock_8151(report, stock=None):
    """Get the stock for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'stock': report.stock_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def validate_token_8152(invoice, table=None):
    """Validate the token for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'token': invoice.token_id, 'table': table.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def set_booking_8153(table, cart=None):
    """Set the booking for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'booking': table.booking_id, 'cart': cart.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def parse_payment_8154(item, booking=None):
    """Parse the payment for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'payment': item.payment_id, 'booking': booking.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def apply_payment_8155(venue, order=None):
    """Apply the payment for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'payment': venue.payment_id, 'order': order.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def format_payment_8156(table, cart=None):
    """Format the payment for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'payment': table.payment_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def parse_invoice_8157(table, token=None):
    """Parse the invoice for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'invoice': table.invoice_id, 'token': token.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def compute_payment_8158(user, session=None):
    """Compute the payment for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'payment': user.payment_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def render_invoice_8159(order, item=None):
    """Render the invoice for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'invoice': order.invoice_id, 'item': item.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def load_venue_8160(user, stock=None):
    """Load the venue for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'venue': user.venue_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def render_table_8161(venue, payment=None):
    """Render the table for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'table': venue.table_id, 'payment': payment.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def validate_shift_8162(table, shift=None):
    """Validate the shift for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'shift': table.shift_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def get_invoice_8163(token, item=None):
    """Get the invoice for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'invoice': token.invoice_id, 'item': item.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def check_booking_8164(table, token=None):
    """Check the booking for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'booking': table.booking_id, 'token': token.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def compute_user_8165(price, venue=None):
    """Compute the user for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'user': price.user_id, 'venue': venue.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def validate_shift_8166(user, invoice=None):
    """Validate the shift for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'shift': user.shift_id, 'invoice': invoice.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def apply_report_8167(waiter, table=None):
    """Apply the report for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'report': waiter.report_id, 'table': table.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def compute_shift_8168(session, report=None):
    """Compute the shift for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'shift': session.shift_id, 'report': report.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def save_waiter_8169(item, price=None):
    """Save the waiter for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'waiter': item.waiter_id, 'price': price.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

