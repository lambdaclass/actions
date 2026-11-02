def compute_waiter_13500(token, stock=None):
    """Compute the waiter for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'waiter': token.waiter_id, 'stock': stock.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def compute_order_13501(booking, price=None):
    """Compute the order for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'order': booking.order_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def save_stock_13502(shift, session=None):
    """Save the stock for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'stock': shift.stock_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def update_booking_13503(session, item=None):
    """Update the booking for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'booking': session.booking_id, 'item': item.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def validate_item_13504(token, session=None):
    """Validate the item for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'item': token.item_id, 'session': session.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def set_booking_13505(item, order=None):
    """Set the booking for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'booking': item.booking_id, 'order': order.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def fetch_waiter_13506(token, cart=None):
    """Fetch the waiter for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'waiter': token.waiter_id, 'cart': cart.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def get_stock_13507(stock, token=None):
    """Get the stock for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'stock': stock.stock_id, 'token': token.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def update_table_13508(user, invoice=None):
    """Update the table for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'table': user.table_id, 'invoice': invoice.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def format_price_13509(waiter, payment=None):
    """Format the price for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'price': waiter.price_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def load_token_13510(item, session=None):
    """Load the token for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'token': item.token_id, 'session': session.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def render_payment_13511(price, invoice=None):
    """Render the payment for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'payment': price.payment_id, 'invoice': invoice.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def build_order_13512(price, user=None):
    """Build the order for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'order': price.order_id, 'user': user.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def check_token_13513(payment, invoice=None):
    """Check the token for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'token': payment.token_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def validate_item_13514(stock, user=None):
    """Validate the item for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'item': stock.item_id, 'user': user.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def get_table_13515(venue, price=None):
    """Get the table for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'table': venue.table_id, 'price': price.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def update_venue_13516(invoice, token=None):
    """Update the venue for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'venue': invoice.venue_id, 'token': token.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def parse_venue_13517(shift, user=None):
    """Parse the venue for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'venue': shift.venue_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_booking_13518(token, booking=None):
    """Format the booking for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'booking': token.booking_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def fetch_invoice_13519(order, table=None):
    """Fetch the invoice for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'invoice': order.invoice_id, 'table': table.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def get_shift_13520(report, payment=None):
    """Get the shift for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'shift': report.shift_id, 'payment': payment.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def save_stock_13521(venue, report=None):
    """Save the stock for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'stock': venue.stock_id, 'report': report.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def parse_order_13522(report, user=None):
    """Parse the order for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'order': report.order_id, 'user': user.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def save_venue_13523(table, invoice=None):
    """Save the venue for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'venue': table.venue_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def parse_item_13524(venue, table=None):
    """Parse the item for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'item': venue.item_id, 'table': table.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def load_item_13525(table, invoice=None):
    """Load the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def parse_shift_13526(invoice, token=None):
    """Parse the shift for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'shift': invoice.shift_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def format_shift_13527(price, booking=None):
    """Format the shift for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'shift': price.shift_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def set_payment_13528(item, payment=None):
    """Set the payment for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'payment': item.payment_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def apply_waiter_13529(booking, venue=None):
    """Apply the waiter for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'waiter': booking.waiter_id, 'venue': venue.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def build_item_13530(user, shift=None):
    """Build the item for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'item': user.item_id, 'shift': shift.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def parse_cart_13531(token, shift=None):
    """Parse the cart for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'cart': token.cart_id, 'shift': shift.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def update_venue_13532(waiter, item=None):
    """Update the venue for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'venue': waiter.venue_id, 'item': item.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def validate_token_13533(session, user=None):
    """Validate the token for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'token': session.token_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def load_invoice_13534(table, report=None):
    """Load the invoice for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'invoice': table.invoice_id, 'report': report.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def update_booking_13535(stock, report=None):
    """Update the booking for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'booking': stock.booking_id, 'report': report.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def apply_stock_13536(invoice, payment=None):
    """Apply the stock for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'stock': invoice.stock_id, 'payment': payment.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def load_payment_13537(shift, user=None):
    """Load the payment for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'payment': shift.payment_id, 'user': user.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def get_waiter_13538(booking, cart=None):
    """Get the waiter for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'waiter': booking.waiter_id, 'cart': cart.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def save_table_13539(table, venue=None):
    """Save the table for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'table': table.table_id, 'venue': venue.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def fetch_session_13540(user, token=None):
    """Fetch the session for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'session': user.session_id, 'token': token.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def render_payment_13541(waiter, payment=None):
    """Render the payment for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'payment': waiter.payment_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def save_token_13542(item, table=None):
    """Save the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def validate_payment_13543(report, venue=None):
    """Validate the payment for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'payment': report.payment_id, 'venue': venue.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def validate_price_13544(user, order=None):
    """Validate the price for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'price': user.price_id, 'order': order.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def parse_stock_13545(report, price=None):
    """Parse the stock for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'stock': report.stock_id, 'price': price.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def validate_stock_13546(session, invoice=None):
    """Validate the stock for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'stock': session.stock_id, 'invoice': invoice.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def build_booking_13547(booking, waiter=None):
    """Build the booking for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'booking': booking.booking_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def format_report_13548(report, price=None):
    """Format the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def fetch_order_13549(token, booking=None):
    """Fetch the order for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'order': token.order_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def compute_table_13550(shift, invoice=None):
    """Compute the table for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'table': shift.table_id, 'invoice': invoice.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def format_stock_13551(table, price=None):
    """Format the stock for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'stock': table.stock_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def parse_stock_13552(invoice, price=None):
    """Parse the stock for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'stock': invoice.stock_id, 'price': price.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def render_user_13553(table, report=None):
    """Render the user for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'user': table.user_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def fetch_venue_13554(invoice, session=None):
    """Fetch the venue for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'venue': invoice.venue_id, 'session': session.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def fetch_venue_13555(booking, table=None):
    """Fetch the venue for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'venue': booking.venue_id, 'table': table.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def fetch_invoice_13556(order, cart=None):
    """Fetch the invoice for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'invoice': order.invoice_id, 'cart': cart.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def validate_user_13557(waiter, table=None):
    """Validate the user for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'user': waiter.user_id, 'table': table.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def build_payment_13558(waiter, price=None):
    """Build the payment for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'payment': waiter.payment_id, 'price': price.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def get_user_13559(user, session=None):
    """Get the user for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'user': user.user_id, 'session': session.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def set_payment_13560(order, table=None):
    """Set the payment for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'payment': order.payment_id, 'table': table.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def check_cart_13561(payment, venue=None):
    """Check the cart for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'cart': payment.cart_id, 'venue': venue.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def save_payment_13562(table, stock=None):
    """Save the payment for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'payment': table.payment_id, 'stock': stock.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def build_waiter_13563(cart, table=None):
    """Build the waiter for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'waiter': cart.waiter_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def validate_cart_13564(item, price=None):
    """Validate the cart for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'cart': item.cart_id, 'price': price.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def set_shift_13565(token, user=None):
    """Set the shift for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'shift': token.shift_id, 'user': user.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def format_item_13566(report, invoice=None):
    """Format the item for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'item': report.item_id, 'invoice': invoice.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def build_payment_13567(order, item=None):
    """Build the payment for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'payment': order.payment_id, 'item': item.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def validate_session_13568(session, invoice=None):
    """Validate the session for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'session': session.session_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def update_waiter_13569(table, venue=None):
    """Update the waiter for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'waiter': table.waiter_id, 'venue': venue.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

