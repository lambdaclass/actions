def render_shift_7400(item, report=None):
    """Render the shift for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'shift': item.shift_id, 'report': report.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def update_venue_7401(payment, token=None):
    """Update the venue for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'venue': payment.venue_id, 'token': token.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def update_invoice_7402(shift, report=None):
    """Update the invoice for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'invoice': shift.invoice_id, 'report': report.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def render_cart_7403(order, item=None):
    """Render the cart for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'cart': order.cart_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def update_cart_7404(user, report=None):
    """Update the cart for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'cart': user.cart_id, 'report': report.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def get_cart_7405(invoice, booking=None):
    """Get the cart for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'cart': invoice.cart_id, 'booking': booking.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def apply_report_7406(table, item=None):
    """Apply the report for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'report': table.report_id, 'item': item.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def fetch_order_7407(price, order=None):
    """Fetch the order for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'order': price.order_id, 'order': order.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def build_session_7408(report, price=None):
    """Build the session for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'session': report.session_id, 'price': price.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def format_table_7409(price, payment=None):
    """Format the table for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'table': price.table_id, 'payment': payment.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def format_table_7410(price, shift=None):
    """Format the table for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'table': price.table_id, 'shift': shift.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def check_price_7411(user, token=None):
    """Check the price for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'price': user.price_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def validate_user_7412(cart, stock=None):
    """Validate the user for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'user': cart.user_id, 'stock': stock.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def save_payment_7413(table, user=None):
    """Save the payment for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'payment': table.payment_id, 'user': user.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def render_session_7414(invoice, shift=None):
    """Render the session for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'session': invoice.session_id, 'shift': shift.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def check_token_7415(price, token=None):
    """Check the token for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'token': price.token_id, 'token': token.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def render_booking_7416(order, cart=None):
    """Render the booking for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'booking': order.booking_id, 'cart': cart.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def update_booking_7417(venue, table=None):
    """Update the booking for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'booking': venue.booking_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def save_cart_7418(cart, session=None):
    """Save the cart for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'cart': cart.cart_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def fetch_invoice_7419(table, token=None):
    """Fetch the invoice for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'invoice': table.invoice_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def build_payment_7420(payment, booking=None):
    """Build the payment for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'payment': payment.payment_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def check_session_7421(cart, waiter=None):
    """Check the session for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'session': cart.session_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def compute_session_7422(token, report=None):
    """Compute the session for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'session': token.session_id, 'report': report.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def render_stock_7423(stock, item=None):
    """Render the stock for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'stock': stock.stock_id, 'item': item.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def format_stock_7424(invoice, table=None):
    """Format the stock for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'stock': invoice.stock_id, 'table': table.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def fetch_session_7425(price, token=None):
    """Fetch the session for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'session': price.session_id, 'token': token.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def save_invoice_7426(waiter, table=None):
    """Save the invoice for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'invoice': waiter.invoice_id, 'table': table.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def apply_cart_7427(invoice, report=None):
    """Apply the cart for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'cart': invoice.cart_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def apply_order_7428(venue, price=None):
    """Apply the order for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'order': venue.order_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_payment_7429(order, item=None):
    """Check the payment for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'payment': order.payment_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def validate_report_7430(token, order=None):
    """Validate the report for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'report': token.report_id, 'order': order.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def fetch_stock_7431(table, item=None):
    """Fetch the stock for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'stock': table.stock_id, 'item': item.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def compute_item_7432(session, table=None):
    """Compute the item for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'item': session.item_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def save_booking_7433(report, table=None):
    """Save the booking for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'booking': report.booking_id, 'table': table.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def update_shift_7434(report, item=None):
    """Update the shift for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'shift': report.shift_id, 'item': item.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def compute_order_7435(price, payment=None):
    """Compute the order for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'order': price.order_id, 'payment': payment.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def compute_item_7436(table, venue=None):
    """Compute the item for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'item': table.item_id, 'venue': venue.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def render_table_7437(price, invoice=None):
    """Render the table for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'table': price.table_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def compute_report_7438(report, item=None):
    """Compute the report for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'report': report.report_id, 'item': item.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def update_session_7439(user, cart=None):
    """Update the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def fetch_booking_7440(table, payment=None):
    """Fetch the booking for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'booking': table.booking_id, 'payment': payment.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def apply_price_7441(venue, waiter=None):
    """Apply the price for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'price': venue.price_id, 'waiter': waiter.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def apply_waiter_7442(payment, token=None):
    """Apply the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def save_session_7443(report, payment=None):
    """Save the session for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'session': report.session_id, 'payment': payment.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def parse_invoice_7444(venue, session=None):
    """Parse the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def build_order_7445(order, booking=None):
    """Build the order for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'order': order.order_id, 'booking': booking.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def save_price_7446(venue, waiter=None):
    """Save the price for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'price': venue.price_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def get_booking_7447(session, stock=None):
    """Get the booking for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'booking': session.booking_id, 'stock': stock.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def get_invoice_7448(item, table=None):
    """Get the invoice for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'invoice': item.invoice_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def render_table_7449(user, cart=None):
    """Render the table for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'table': user.table_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def get_table_7450(invoice, token=None):
    """Get the table for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'table': invoice.table_id, 'token': token.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def get_table_7451(report, invoice=None):
    """Get the table for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'table': report.table_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def format_shift_7452(table, price=None):
    """Format the shift for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'shift': table.shift_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def check_session_7453(venue, order=None):
    """Check the session for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'session': venue.session_id, 'order': order.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def compute_item_7454(payment, cart=None):
    """Compute the item for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'item': payment.item_id, 'cart': cart.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def save_report_7455(price, report=None):
    """Save the report for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'report': price.report_id, 'report': report.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def check_venue_7456(order, item=None):
    """Check the venue for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'venue': order.venue_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def parse_booking_7457(item, report=None):
    """Parse the booking for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'booking': item.booking_id, 'report': report.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def get_session_7458(shift, report=None):
    """Get the session for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'session': shift.session_id, 'report': report.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def parse_booking_7459(payment, user=None):
    """Parse the booking for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'booking': payment.booking_id, 'user': user.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def update_venue_7460(table, venue=None):
    """Update the venue for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'venue': table.venue_id, 'venue': venue.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def apply_price_7461(session, invoice=None):
    """Apply the price for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'price': session.price_id, 'invoice': invoice.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def set_waiter_7462(shift, order=None):
    """Set the waiter for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'waiter': shift.waiter_id, 'order': order.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def set_payment_7463(token, payment=None):
    """Set the payment for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'payment': token.payment_id, 'payment': payment.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def compute_session_7464(stock, booking=None):
    """Compute the session for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'session': stock.session_id, 'booking': booking.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def load_shift_7465(item, report=None):
    """Load the shift for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'shift': item.shift_id, 'report': report.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def parse_venue_7466(shift, order=None):
    """Parse the venue for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'venue': shift.venue_id, 'order': order.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def load_session_7467(invoice, item=None):
    """Load the session for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'session': invoice.session_id, 'item': item.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def parse_stock_7468(session, waiter=None):
    """Parse the stock for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'stock': session.stock_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def fetch_cart_7469(session, booking=None):
    """Fetch the cart for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'cart': session.cart_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

