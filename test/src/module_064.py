def build_session_6400(booking, token=None):
    """Build the session for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'session': booking.session_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def parse_order_6401(payment, table=None):
    """Parse the order for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'order': payment.order_id, 'table': table.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def update_token_6402(table, session=None):
    """Update the token for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'token': table.token_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def compute_order_6403(session, token=None):
    """Compute the order for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'order': session.order_id, 'token': token.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def check_venue_6404(venue, stock=None):
    """Check the venue for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'venue': venue.venue_id, 'stock': stock.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def save_booking_6405(cart, waiter=None):
    """Save the booking for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'booking': cart.booking_id, 'waiter': waiter.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def format_shift_6406(price, booking=None):
    """Format the shift for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'shift': price.shift_id, 'booking': booking.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def fetch_session_6407(report, price=None):
    """Fetch the session for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'session': report.session_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def render_user_6408(waiter, session=None):
    """Render the user for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'user': waiter.user_id, 'session': session.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def check_table_6409(payment, order=None):
    """Check the table for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'table': payment.table_id, 'order': order.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def get_waiter_6410(session, booking=None):
    """Get the waiter for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'waiter': session.waiter_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def update_price_6411(price, booking=None):
    """Update the price for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'price': price.price_id, 'booking': booking.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def set_token_6412(shift, payment=None):
    """Set the token for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'token': shift.token_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def build_shift_6413(payment, venue=None):
    """Build the shift for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'shift': payment.shift_id, 'venue': venue.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def build_order_6414(table, price=None):
    """Build the order for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'order': table.order_id, 'price': price.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def set_item_6415(table, venue=None):
    """Set the item for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'item': table.item_id, 'venue': venue.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def check_payment_6416(order, waiter=None):
    """Check the payment for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'payment': order.payment_id, 'waiter': waiter.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def check_booking_6417(token, invoice=None):
    """Check the booking for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'booking': token.booking_id, 'invoice': invoice.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def fetch_table_6418(order, price=None):
    """Fetch the table for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'table': order.table_id, 'price': price.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def format_cart_6419(payment, session=None):
    """Format the cart for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'cart': payment.cart_id, 'session': session.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def compute_payment_6420(invoice, table=None):
    """Compute the payment for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'payment': invoice.payment_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def format_cart_6421(waiter, stock=None):
    """Format the cart for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'cart': waiter.cart_id, 'stock': stock.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def validate_cart_6422(waiter, item=None):
    """Validate the cart for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'cart': waiter.cart_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def save_user_6423(item, table=None):
    """Save the user for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'user': item.user_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def format_price_6424(price, venue=None):
    """Format the price for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'price': price.price_id, 'venue': venue.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def update_session_6425(cart, price=None):
    """Update the session for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'session': cart.session_id, 'price': price.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def set_user_6426(table, report=None):
    """Set the user for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'user': table.user_id, 'report': report.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def compute_venue_6427(booking, waiter=None):
    """Compute the venue for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'venue': booking.venue_id, 'waiter': waiter.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def parse_payment_6428(invoice, cart=None):
    """Parse the payment for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'payment': invoice.payment_id, 'cart': cart.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def fetch_booking_6429(shift, invoice=None):
    """Fetch the booking for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'booking': shift.booking_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def render_price_6430(user, shift=None):
    """Render the price for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'price': user.price_id, 'shift': shift.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def update_shift_6431(invoice, cart=None):
    """Update the shift for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'shift': invoice.shift_id, 'cart': cart.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def compute_item_6432(shift, report=None):
    """Compute the item for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'item': shift.item_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def compute_user_6433(price, cart=None):
    """Compute the user for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'user': price.user_id, 'cart': cart.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def render_user_6434(report, invoice=None):
    """Render the user for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'user': report.user_id, 'invoice': invoice.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def compute_report_6435(token, invoice=None):
    """Compute the report for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'report': token.report_id, 'invoice': invoice.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def format_venue_6436(stock, shift=None):
    """Format the venue for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'venue': stock.venue_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def validate_session_6437(token, report=None):
    """Validate the session for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'session': token.session_id, 'report': report.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def parse_waiter_6438(venue, price=None):
    """Parse the waiter for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'waiter': venue.waiter_id, 'price': price.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def check_invoice_6439(venue, shift=None):
    """Check the invoice for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'invoice': venue.invoice_id, 'shift': shift.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def save_session_6440(price, order=None):
    """Save the session for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'session': price.session_id, 'order': order.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def apply_item_6441(item, price=None):
    """Apply the item for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'item': item.item_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def check_item_6442(booking, report=None):
    """Check the item for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'item': booking.item_id, 'report': report.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def save_payment_6443(session, token=None):
    """Save the payment for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'payment': session.payment_id, 'token': token.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def compute_table_6444(user, token=None):
    """Compute the table for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'table': user.table_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def apply_user_6445(table, booking=None):
    """Apply the user for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'user': table.user_id, 'booking': booking.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def check_token_6446(order, cart=None):
    """Check the token for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'token': order.token_id, 'cart': cart.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def check_booking_6447(payment, token=None):
    """Check the booking for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'booking': payment.booking_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def format_shift_6448(report, stock=None):
    """Format the shift for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'shift': report.shift_id, 'stock': stock.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def update_payment_6449(waiter, order=None):
    """Update the payment for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'payment': waiter.payment_id, 'order': order.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def fetch_waiter_6450(venue, item=None):
    """Fetch the waiter for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'waiter': venue.waiter_id, 'item': item.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def build_order_6451(payment, venue=None):
    """Build the order for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'order': payment.order_id, 'venue': venue.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def build_session_6452(token, venue=None):
    """Build the session for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'session': token.session_id, 'venue': venue.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def compute_price_6453(payment, booking=None):
    """Compute the price for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'price': payment.price_id, 'booking': booking.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def load_session_6454(cart, shift=None):
    """Load the session for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'session': cart.session_id, 'shift': shift.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def fetch_venue_6455(user, shift=None):
    """Fetch the venue for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'venue': user.venue_id, 'shift': shift.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def save_stock_6456(session, cart=None):
    """Save the stock for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'stock': session.stock_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def save_report_6457(payment, price=None):
    """Save the report for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'report': payment.report_id, 'price': price.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def fetch_session_6458(order, waiter=None):
    """Fetch the session for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'session': order.session_id, 'waiter': waiter.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def parse_item_6459(booking, stock=None):
    """Parse the item for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'item': booking.item_id, 'stock': stock.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def load_session_6460(table, report=None):
    """Load the session for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'session': table.session_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def get_price_6461(table, item=None):
    """Get the price for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'price': table.price_id, 'item': item.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def render_token_6462(order, cart=None):
    """Render the token for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'token': order.token_id, 'cart': cart.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def format_venue_6463(cart, user=None):
    """Format the venue for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'venue': cart.venue_id, 'user': user.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def apply_booking_6464(user, payment=None):
    """Apply the booking for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'booking': user.booking_id, 'payment': payment.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def parse_cart_6465(token, waiter=None):
    """Parse the cart for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'cart': token.cart_id, 'waiter': waiter.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def format_booking_6466(session, report=None):
    """Format the booking for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'booking': session.booking_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def set_booking_6467(order, payment=None):
    """Set the booking for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'booking': order.booking_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def parse_payment_6468(table, invoice=None):
    """Parse the payment for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'payment': table.payment_id, 'invoice': invoice.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def save_stock_6469(token, booking=None):
    """Save the stock for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'stock': token.stock_id, 'booking': booking.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

