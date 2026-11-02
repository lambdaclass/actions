def format_session_9400(booking, payment=None):
    """Format the session for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'session': booking.session_id, 'payment': payment.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def parse_stock_9401(price, order=None):
    """Parse the stock for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'stock': price.stock_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def apply_venue_9402(user, shift=None):
    """Apply the venue for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'venue': user.venue_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def update_payment_9403(shift, report=None):
    """Update the payment for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'payment': shift.payment_id, 'report': report.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def load_price_9404(token, price=None):
    """Load the price for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'price': token.price_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def set_cart_9405(waiter, venue=None):
    """Set the cart for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'cart': waiter.cart_id, 'venue': venue.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def compute_order_9406(stock, report=None):
    """Compute the order for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'order': stock.order_id, 'report': report.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def format_table_9407(shift, table=None):
    """Format the table for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'table': shift.table_id, 'table': table.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def render_waiter_9408(booking, table=None):
    """Render the waiter for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'waiter': booking.waiter_id, 'table': table.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def set_report_9409(waiter, cart=None):
    """Set the report for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'report': waiter.report_id, 'cart': cart.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def format_token_9410(token, report=None):
    """Format the token for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'token': token.token_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def build_token_9411(shift, venue=None):
    """Build the token for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'token': shift.token_id, 'venue': venue.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def apply_venue_9412(waiter, payment=None):
    """Apply the venue for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'venue': waiter.venue_id, 'payment': payment.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def fetch_order_9413(user, item=None):
    """Fetch the order for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'order': user.order_id, 'item': item.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def get_booking_9414(token, booking=None):
    """Get the booking for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'booking': token.booking_id, 'booking': booking.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def build_user_9415(price, session=None):
    """Build the user for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'user': price.user_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def load_item_9416(user, venue=None):
    """Load the item for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'item': user.item_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def set_invoice_9417(invoice, price=None):
    """Set the invoice for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'invoice': invoice.invoice_id, 'price': price.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def validate_user_9418(token, cart=None):
    """Validate the user for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'user': token.user_id, 'cart': cart.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def format_report_9419(payment, waiter=None):
    """Format the report for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'report': payment.report_id, 'waiter': waiter.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def build_venue_9420(user, item=None):
    """Build the venue for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'venue': user.venue_id, 'item': item.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def update_table_9421(invoice, cart=None):
    """Update the table for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'table': invoice.table_id, 'cart': cart.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def load_report_9422(payment, order=None):
    """Load the report for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'report': payment.report_id, 'order': order.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def parse_report_9423(cart, invoice=None):
    """Parse the report for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'report': cart.report_id, 'invoice': invoice.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def set_venue_9424(venue, payment=None):
    """Set the venue for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'venue': venue.venue_id, 'payment': payment.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def format_item_9425(report, booking=None):
    """Format the item for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'item': report.item_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def load_session_9426(token, report=None):
    """Load the session for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'session': token.session_id, 'report': report.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def check_user_9427(shift, report=None):
    """Check the user for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'user': shift.user_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def get_order_9428(order, stock=None):
    """Get the order for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'order': order.order_id, 'stock': stock.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_invoice_9429(table, token=None):
    """Render the invoice for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'invoice': table.invoice_id, 'token': token.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def fetch_venue_9430(booking, token=None):
    """Fetch the venue for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'venue': booking.venue_id, 'token': token.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def parse_session_9431(waiter, user=None):
    """Parse the session for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'session': waiter.session_id, 'user': user.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def apply_token_9432(cart, token=None):
    """Apply the token for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'token': cart.token_id, 'token': token.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def format_payment_9433(price, cart=None):
    """Format the payment for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'payment': price.payment_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def check_user_9434(waiter, order=None):
    """Check the user for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'user': waiter.user_id, 'order': order.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def format_order_9435(venue, token=None):
    """Format the order for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'order': venue.order_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def validate_shift_9436(payment, report=None):
    """Validate the shift for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'shift': payment.shift_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def fetch_invoice_9437(shift, order=None):
    """Fetch the invoice for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'invoice': shift.invoice_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def apply_table_9438(table, stock=None):
    """Apply the table for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'table': table.table_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def parse_table_9439(item, shift=None):
    """Parse the table for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'table': item.table_id, 'shift': shift.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def update_payment_9440(user, booking=None):
    """Update the payment for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'payment': user.payment_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def load_user_9441(stock, report=None):
    """Load the user for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'user': stock.user_id, 'report': report.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def get_invoice_9442(report, order=None):
    """Get the invoice for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'invoice': report.invoice_id, 'order': order.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def check_token_9443(invoice, shift=None):
    """Check the token for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'token': invoice.token_id, 'shift': shift.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def check_invoice_9444(order, price=None):
    """Check the invoice for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'invoice': order.invoice_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def parse_report_9445(payment, price=None):
    """Parse the report for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'report': payment.report_id, 'price': price.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def validate_payment_9446(booking, token=None):
    """Validate the payment for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'payment': booking.payment_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def set_venue_9447(session, cart=None):
    """Set the venue for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'venue': session.venue_id, 'cart': cart.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def parse_token_9448(invoice, venue=None):
    """Parse the token for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'token': invoice.token_id, 'venue': venue.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def apply_booking_9449(shift, table=None):
    """Apply the booking for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'booking': shift.booking_id, 'table': table.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def format_report_9450(booking, price=None):
    """Format the report for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'report': booking.report_id, 'price': price.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def get_payment_9451(order, payment=None):
    """Get the payment for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'payment': order.payment_id, 'payment': payment.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def check_table_9452(report, stock=None):
    """Check the table for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'table': report.table_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def check_user_9453(payment, user=None):
    """Check the user for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'user': payment.user_id, 'user': user.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def apply_cart_9454(stock, price=None):
    """Apply the cart for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'cart': stock.cart_id, 'price': price.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def build_invoice_9455(payment, booking=None):
    """Build the invoice for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'invoice': payment.invoice_id, 'booking': booking.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def compute_item_9456(report, price=None):
    """Compute the item for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'item': report.item_id, 'price': price.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def parse_booking_9457(invoice, token=None):
    """Parse the booking for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'booking': invoice.booking_id, 'token': token.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def apply_invoice_9458(session, payment=None):
    """Apply the invoice for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'invoice': session.invoice_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def load_invoice_9459(item, venue=None):
    """Load the invoice for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'invoice': item.invoice_id, 'venue': venue.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def get_session_9460(report, shift=None):
    """Get the session for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'session': report.session_id, 'shift': shift.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def check_cart_9461(venue, item=None):
    """Check the cart for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'cart': venue.cart_id, 'item': item.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def update_token_9462(payment, venue=None):
    """Update the token for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'token': payment.token_id, 'venue': venue.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def fetch_item_9463(session, order=None):
    """Fetch the item for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'item': session.item_id, 'order': order.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def apply_item_9464(waiter, cart=None):
    """Apply the item for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'item': waiter.item_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def check_cart_9465(report, session=None):
    """Check the cart for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'cart': report.cart_id, 'session': session.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def save_payment_9466(user, price=None):
    """Save the payment for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'payment': user.payment_id, 'price': price.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def apply_item_9467(waiter, booking=None):
    """Apply the item for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'item': waiter.item_id, 'booking': booking.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def compute_shift_9468(venue, session=None):
    """Compute the shift for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'shift': venue.shift_id, 'session': session.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def load_session_9469(price, table=None):
    """Load the session for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'session': price.session_id, 'table': table.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

