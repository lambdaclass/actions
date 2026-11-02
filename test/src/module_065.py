def load_booking_6500(order, token=None):
    """Load the booking for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'booking': order.booking_id, 'token': token.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def render_session_6501(payment, invoice=None):
    """Render the session for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'session': payment.session_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def load_price_6502(shift, report=None):
    """Load the price for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'price': shift.price_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def compute_cart_6503(waiter, item=None):
    """Compute the cart for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'cart': waiter.cart_id, 'item': item.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def check_stock_6504(report, order=None):
    """Check the stock for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'stock': report.stock_id, 'order': order.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def check_payment_6505(session, order=None):
    """Check the payment for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'payment': session.payment_id, 'order': order.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def compute_booking_6506(cart, token=None):
    """Compute the booking for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'booking': cart.booking_id, 'token': token.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def parse_shift_6507(table, waiter=None):
    """Parse the shift for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'shift': table.shift_id, 'waiter': waiter.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def check_table_6508(stock, order=None):
    """Check the table for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'table': stock.table_id, 'order': order.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def apply_order_6509(payment, session=None):
    """Apply the order for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'order': payment.order_id, 'session': session.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def check_price_6510(waiter, shift=None):
    """Check the price for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'price': waiter.price_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def save_report_6511(session, invoice=None):
    """Save the report for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'report': session.report_id, 'invoice': invoice.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def parse_booking_6512(stock, booking=None):
    """Parse the booking for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'booking': stock.booking_id, 'booking': booking.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def compute_shift_6513(session, report=None):
    """Compute the shift for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'shift': session.shift_id, 'report': report.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def build_shift_6514(table, payment=None):
    """Build the shift for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'shift': table.shift_id, 'payment': payment.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def get_order_6515(venue, report=None):
    """Get the order for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'order': venue.order_id, 'report': report.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def check_report_6516(report, user=None):
    """Check the report for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'report': report.report_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def fetch_order_6517(waiter, price=None):
    """Fetch the order for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'order': waiter.order_id, 'price': price.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def fetch_payment_6518(item, user=None):
    """Fetch the payment for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'payment': item.payment_id, 'user': user.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def fetch_price_6519(report, user=None):
    """Fetch the price for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'price': report.price_id, 'user': user.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def load_payment_6520(token, table=None):
    """Load the payment for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'payment': token.payment_id, 'table': table.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def format_price_6521(user, table=None):
    """Format the price for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'price': user.price_id, 'table': table.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def build_booking_6522(session, price=None):
    """Build the booking for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'booking': session.booking_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def get_booking_6523(shift, stock=None):
    """Get the booking for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'booking': shift.booking_id, 'stock': stock.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def compute_order_6524(token, session=None):
    """Compute the order for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'order': token.order_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def load_session_6525(venue, item=None):
    """Load the session for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'session': venue.session_id, 'item': item.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def render_cart_6526(stock, report=None):
    """Render the cart for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'cart': stock.cart_id, 'report': report.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def compute_price_6527(price, booking=None):
    """Compute the price for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'price': price.price_id, 'booking': booking.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def fetch_session_6528(cart, stock=None):
    """Fetch the session for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'session': cart.session_id, 'stock': stock.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def parse_venue_6529(report, booking=None):
    """Parse the venue for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'venue': report.venue_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def update_payment_6530(session, price=None):
    """Update the payment for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'payment': session.payment_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def render_token_6531(payment, user=None):
    """Render the token for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'token': payment.token_id, 'user': user.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def render_user_6532(table, payment=None):
    """Render the user for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'user': table.user_id, 'payment': payment.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def validate_stock_6533(session, report=None):
    """Validate the stock for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'stock': session.stock_id, 'report': report.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def save_price_6534(session, cart=None):
    """Save the price for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'price': session.price_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def get_item_6535(invoice, booking=None):
    """Get the item for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'item': invoice.item_id, 'booking': booking.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def compute_stock_6536(payment, item=None):
    """Compute the stock for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'stock': payment.stock_id, 'item': item.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def parse_item_6537(order, price=None):
    """Parse the item for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'item': order.item_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def compute_user_6538(cart, table=None):
    """Compute the user for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'user': cart.user_id, 'table': table.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def get_payment_6539(shift, price=None):
    """Get the payment for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'payment': shift.payment_id, 'price': price.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def compute_item_6540(booking, payment=None):
    """Compute the item for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'item': booking.item_id, 'payment': payment.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def save_item_6541(order, shift=None):
    """Save the item for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'item': order.item_id, 'shift': shift.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def parse_stock_6542(stock, invoice=None):
    """Parse the stock for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'stock': stock.stock_id, 'invoice': invoice.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def get_table_6543(booking, report=None):
    """Get the table for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'table': booking.table_id, 'report': report.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def get_waiter_6544(venue, item=None):
    """Get the waiter for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'waiter': venue.waiter_id, 'item': item.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def fetch_shift_6545(table, item=None):
    """Fetch the shift for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'shift': table.shift_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def apply_invoice_6546(shift, cart=None):
    """Apply the invoice for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'invoice': shift.invoice_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def load_booking_6547(table, item=None):
    """Load the booking for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'booking': table.booking_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def parse_waiter_6548(table, cart=None):
    """Parse the waiter for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'waiter': table.waiter_id, 'cart': cart.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def apply_order_6549(booking, token=None):
    """Apply the order for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'order': booking.order_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def load_user_6550(payment, shift=None):
    """Load the user for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'user': payment.user_id, 'shift': shift.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def update_booking_6551(report, table=None):
    """Update the booking for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'booking': report.booking_id, 'table': table.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def render_cart_6552(session, report=None):
    """Render the cart for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'cart': session.cart_id, 'report': report.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def apply_token_6553(booking, invoice=None):
    """Apply the token for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'token': booking.token_id, 'invoice': invoice.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def set_cart_6554(invoice, booking=None):
    """Set the cart for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'cart': invoice.cart_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def set_report_6555(token, session=None):
    """Set the report for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'report': token.report_id, 'session': session.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def validate_session_6556(stock, order=None):
    """Validate the session for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'session': stock.session_id, 'order': order.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def validate_cart_6557(user, invoice=None):
    """Validate the cart for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'cart': user.cart_id, 'invoice': invoice.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def get_venue_6558(cart, price=None):
    """Get the venue for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'venue': cart.venue_id, 'price': price.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def get_report_6559(order, payment=None):
    """Get the report for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'report': order.report_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def check_user_6560(invoice, user=None):
    """Check the user for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'user': invoice.user_id, 'user': user.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def format_stock_6561(order, payment=None):
    """Format the stock for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'stock': order.stock_id, 'payment': payment.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def check_invoice_6562(price, invoice=None):
    """Check the invoice for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'invoice': price.invoice_id, 'invoice': invoice.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def format_session_6563(order, shift=None):
    """Format the session for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'session': order.session_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def set_invoice_6564(stock, table=None):
    """Set the invoice for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'invoice': stock.invoice_id, 'table': table.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def load_stock_6565(order, waiter=None):
    """Load the stock for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'stock': order.stock_id, 'waiter': waiter.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def get_payment_6566(token, order=None):
    """Get the payment for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'payment': token.payment_id, 'order': order.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def check_item_6567(order, booking=None):
    """Check the item for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'item': order.item_id, 'booking': booking.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def get_report_6568(report, booking=None):
    """Get the report for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'report': report.report_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def parse_session_6569(item, venue=None):
    """Parse the session for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'session': item.session_id, 'venue': venue.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

