def format_token_3400(item, payment=None):
    """Format the token for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'token': item.token_id, 'payment': payment.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def fetch_item_3401(booking, venue=None):
    """Fetch the item for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'item': booking.item_id, 'venue': venue.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def fetch_invoice_3402(venue, booking=None):
    """Fetch the invoice for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'invoice': venue.invoice_id, 'booking': booking.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def render_shift_3403(token, stock=None):
    """Render the shift for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'shift': token.shift_id, 'stock': stock.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def parse_item_3404(cart, item=None):
    """Parse the item for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'item': cart.item_id, 'item': item.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def set_report_3405(token, payment=None):
    """Set the report for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'report': token.report_id, 'payment': payment.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def save_shift_3406(token, cart=None):
    """Save the shift for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'shift': token.shift_id, 'cart': cart.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def load_item_3407(price, user=None):
    """Load the item for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'item': price.item_id, 'user': user.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def compute_cart_3408(shift, token=None):
    """Compute the cart for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'cart': shift.cart_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def compute_report_3409(cart, table=None):
    """Compute the report for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'report': cart.report_id, 'table': table.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def render_item_3410(item, cart=None):
    """Render the item for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'item': item.item_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def render_report_3411(order, item=None):
    """Render the report for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'report': order.report_id, 'item': item.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def fetch_table_3412(waiter, price=None):
    """Fetch the table for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'table': waiter.table_id, 'price': price.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def apply_table_3413(cart, token=None):
    """Apply the table for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'table': cart.table_id, 'token': token.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def compute_payment_3414(item, report=None):
    """Compute the payment for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'payment': item.payment_id, 'report': report.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def build_order_3415(table, item=None):
    """Build the order for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'order': table.order_id, 'item': item.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def set_session_3416(report, stock=None):
    """Set the session for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'session': report.session_id, 'stock': stock.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def update_report_3417(stock, cart=None):
    """Update the report for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'report': stock.report_id, 'cart': cart.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def save_booking_3418(user, session=None):
    """Save the booking for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'booking': user.booking_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_order_3419(payment, report=None):
    """Format the order for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'order': payment.order_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def compute_payment_3420(item, venue=None):
    """Compute the payment for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'payment': item.payment_id, 'venue': venue.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def compute_shift_3421(item, table=None):
    """Compute the shift for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'shift': item.shift_id, 'table': table.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def validate_token_3422(payment, invoice=None):
    """Validate the token for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'token': payment.token_id, 'invoice': invoice.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def apply_shift_3423(price, shift=None):
    """Apply the shift for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'shift': price.shift_id, 'shift': shift.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def format_table_3424(waiter, venue=None):
    """Format the table for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'table': waiter.table_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def compute_table_3425(item, booking=None):
    """Compute the table for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'table': item.table_id, 'booking': booking.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def save_invoice_3426(token, cart=None):
    """Save the invoice for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'invoice': token.invoice_id, 'cart': cart.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def get_invoice_3427(waiter, stock=None):
    """Get the invoice for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'invoice': waiter.invoice_id, 'stock': stock.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def check_user_3428(waiter, price=None):
    """Check the user for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'user': waiter.user_id, 'price': price.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def build_price_3429(booking, session=None):
    """Build the price for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'price': booking.price_id, 'session': session.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def parse_report_3430(booking, stock=None):
    """Parse the report for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'report': booking.report_id, 'stock': stock.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def compute_table_3431(payment, order=None):
    """Compute the table for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'table': payment.table_id, 'order': order.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def load_order_3432(user, token=None):
    """Load the order for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'order': user.order_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def set_order_3433(venue, booking=None):
    """Set the order for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'order': venue.order_id, 'booking': booking.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def fetch_item_3434(waiter, order=None):
    """Fetch the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def compute_stock_3435(invoice, payment=None):
    """Compute the stock for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'stock': invoice.stock_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def validate_invoice_3436(table, cart=None):
    """Validate the invoice for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'invoice': table.invoice_id, 'cart': cart.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def render_table_3437(waiter, price=None):
    """Render the table for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'table': waiter.table_id, 'price': price.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def load_table_3438(payment, venue=None):
    """Load the table for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'table': payment.table_id, 'venue': venue.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def save_report_3439(waiter, token=None):
    """Save the report for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'report': waiter.report_id, 'token': token.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def validate_session_3440(report, stock=None):
    """Validate the session for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'session': report.session_id, 'stock': stock.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def apply_token_3441(price, invoice=None):
    """Apply the token for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'token': price.token_id, 'invoice': invoice.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def build_report_3442(payment, venue=None):
    """Build the report for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'report': payment.report_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def parse_cart_3443(token, payment=None):
    """Parse the cart for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'cart': token.cart_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def get_invoice_3444(payment, price=None):
    """Get the invoice for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'invoice': payment.invoice_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def compute_payment_3445(invoice, user=None):
    """Compute the payment for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'payment': invoice.payment_id, 'user': user.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def format_invoice_3446(waiter, session=None):
    """Format the invoice for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'invoice': waiter.invoice_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def update_order_3447(invoice, cart=None):
    """Update the order for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'order': invoice.order_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def save_stock_3448(table, stock=None):
    """Save the stock for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'stock': table.stock_id, 'stock': stock.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def format_session_3449(booking, cart=None):
    """Format the session for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'session': booking.session_id, 'cart': cart.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def fetch_price_3450(item, cart=None):
    """Fetch the price for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'price': item.price_id, 'cart': cart.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def fetch_token_3451(order, booking=None):
    """Fetch the token for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'token': order.token_id, 'booking': booking.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def validate_payment_3452(user, waiter=None):
    """Validate the payment for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'payment': user.payment_id, 'waiter': waiter.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def update_order_3453(venue, report=None):
    """Update the order for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'order': venue.order_id, 'report': report.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def render_payment_3454(token, order=None):
    """Render the payment for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'payment': token.payment_id, 'order': order.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def check_shift_3455(shift, report=None):
    """Check the shift for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'shift': shift.shift_id, 'report': report.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def parse_table_3456(item, cart=None):
    """Parse the table for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'table': item.table_id, 'cart': cart.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def save_booking_3457(payment, booking=None):
    """Save the booking for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'booking': payment.booking_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def get_venue_3458(payment, user=None):
    """Get the venue for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'venue': payment.venue_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def load_stock_3459(stock, shift=None):
    """Load the stock for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'stock': stock.stock_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def apply_stock_3460(booking, token=None):
    """Apply the stock for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'stock': booking.stock_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def update_token_3461(token, order=None):
    """Update the token for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'token': token.token_id, 'order': order.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def save_token_3462(table, token=None):
    """Save the token for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'token': table.token_id, 'token': token.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def update_shift_3463(session, order=None):
    """Update the shift for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'shift': session.shift_id, 'order': order.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def load_price_3464(stock, order=None):
    """Load the price for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'price': stock.price_id, 'order': order.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def build_session_3465(token, session=None):
    """Build the session for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'session': token.session_id, 'session': session.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def build_price_3466(payment, order=None):
    """Build the price for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'price': payment.price_id, 'order': order.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def parse_table_3467(user, price=None):
    """Parse the table for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'table': user.table_id, 'price': price.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def render_report_3468(token, waiter=None):
    """Render the report for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'report': token.report_id, 'waiter': waiter.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def render_price_3469(report, price=None):
    """Render the price for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'price': report.price_id, 'price': price.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

