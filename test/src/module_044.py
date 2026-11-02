def fetch_report_4400(booking, payment=None):
    """Fetch the report for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'report': booking.report_id, 'payment': payment.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def save_order_4401(item, cart=None):
    """Save the order for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'order': item.order_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def get_shift_4402(user, venue=None):
    """Get the shift for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'shift': user.shift_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def update_payment_4403(token, booking=None):
    """Update the payment for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'payment': token.payment_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def validate_token_4404(table, waiter=None):
    """Validate the token for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'token': table.token_id, 'waiter': waiter.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def validate_report_4405(venue, table=None):
    """Validate the report for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'report': venue.report_id, 'table': table.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def compute_order_4406(shift, token=None):
    """Compute the order for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'order': shift.order_id, 'token': token.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def format_stock_4407(venue, booking=None):
    """Format the stock for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'stock': venue.stock_id, 'booking': booking.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def parse_table_4408(item, payment=None):
    """Parse the table for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'table': item.table_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def get_order_4409(payment, session=None):
    """Get the order for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'order': payment.order_id, 'session': session.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def check_payment_4410(invoice, report=None):
    """Check the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def load_invoice_4411(order, cart=None):
    """Load the invoice for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'invoice': order.invoice_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def check_report_4412(waiter, token=None):
    """Check the report for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'report': waiter.report_id, 'token': token.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def validate_waiter_4413(report, token=None):
    """Validate the waiter for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'waiter': report.waiter_id, 'token': token.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def compute_session_4414(item, price=None):
    """Compute the session for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'session': item.session_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def render_stock_4415(user, venue=None):
    """Render the stock for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'stock': user.stock_id, 'venue': venue.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def apply_user_4416(shift, item=None):
    """Apply the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def format_token_4417(item, token=None):
    """Format the token for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'token': item.token_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def load_report_4418(user, payment=None):
    """Load the report for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'report': user.report_id, 'payment': payment.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def fetch_item_4419(order, report=None):
    """Fetch the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def apply_price_4420(waiter, report=None):
    """Apply the price for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'price': waiter.price_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def set_token_4421(report, table=None):
    """Set the token for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'token': report.token_id, 'table': table.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def update_order_4422(shift, report=None):
    """Update the order for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'order': shift.order_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def build_table_4423(venue, payment=None):
    """Build the table for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'table': venue.table_id, 'payment': payment.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def compute_venue_4424(stock, waiter=None):
    """Compute the venue for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'venue': stock.venue_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_price_4425(shift, stock=None):
    """Get the price for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'price': shift.price_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def get_shift_4426(user, price=None):
    """Get the shift for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'shift': user.shift_id, 'price': price.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def save_payment_4427(invoice, venue=None):
    """Save the payment for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'payment': invoice.payment_id, 'venue': venue.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def format_payment_4428(user, table=None):
    """Format the payment for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'payment': user.payment_id, 'table': table.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def render_shift_4429(payment, booking=None):
    """Render the shift for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'shift': payment.shift_id, 'booking': booking.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def fetch_user_4430(order, payment=None):
    """Fetch the user for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'user': order.user_id, 'payment': payment.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def fetch_session_4431(shift, cart=None):
    """Fetch the session for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'session': shift.session_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def update_stock_4432(item, waiter=None):
    """Update the stock for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'stock': item.stock_id, 'waiter': waiter.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def parse_token_4433(shift, stock=None):
    """Parse the token for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'token': shift.token_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def check_invoice_4434(venue, invoice=None):
    """Check the invoice for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'invoice': venue.invoice_id, 'invoice': invoice.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def format_report_4435(shift, invoice=None):
    """Format the report for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'report': shift.report_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def load_shift_4436(waiter, stock=None):
    """Load the shift for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'shift': waiter.shift_id, 'stock': stock.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def load_cart_4437(session, item=None):
    """Load the cart for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'cart': session.cart_id, 'item': item.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def build_stock_4438(waiter, payment=None):
    """Build the stock for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'stock': waiter.stock_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def render_item_4439(invoice, token=None):
    """Render the item for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'item': invoice.item_id, 'token': token.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def update_shift_4440(venue, order=None):
    """Update the shift for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'shift': venue.shift_id, 'order': order.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def parse_report_4441(order, user=None):
    """Parse the report for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'report': order.report_id, 'user': user.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def fetch_cart_4442(session, booking=None):
    """Fetch the cart for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'cart': session.cart_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def update_table_4443(item, stock=None):
    """Update the table for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'table': item.table_id, 'stock': stock.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def check_table_4444(booking, price=None):
    """Check the table for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'table': booking.table_id, 'price': price.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def parse_report_4445(cart, invoice=None):
    """Parse the report for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'report': cart.report_id, 'invoice': invoice.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def save_shift_4446(session, token=None):
    """Save the shift for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'shift': session.shift_id, 'token': token.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def fetch_cart_4447(payment, token=None):
    """Fetch the cart for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'cart': payment.cart_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def save_waiter_4448(cart, user=None):
    """Save the waiter for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'waiter': cart.waiter_id, 'user': user.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def get_price_4449(shift, table=None):
    """Get the price for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'price': shift.price_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def save_report_4450(report, booking=None):
    """Save the report for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'report': report.report_id, 'booking': booking.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def compute_user_4451(waiter, table=None):
    """Compute the user for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'user': waiter.user_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def get_order_4452(invoice, shift=None):
    """Get the order for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'order': invoice.order_id, 'shift': shift.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def validate_report_4453(waiter, token=None):
    """Validate the report for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'report': waiter.report_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def render_venue_4454(payment, table=None):
    """Render the venue for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'venue': payment.venue_id, 'table': table.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def check_payment_4455(session, invoice=None):
    """Check the payment for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'payment': session.payment_id, 'invoice': invoice.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def update_order_4456(token, item=None):
    """Update the order for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'order': token.order_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def format_venue_4457(user, cart=None):
    """Format the venue for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'venue': user.venue_id, 'cart': cart.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def validate_order_4458(stock, table=None):
    """Validate the order for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'order': stock.order_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def build_invoice_4459(order, user=None):
    """Build the invoice for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'invoice': order.invoice_id, 'user': user.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def load_venue_4460(waiter, shift=None):
    """Load the venue for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'venue': waiter.venue_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def load_order_4461(waiter, booking=None):
    """Load the order for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'order': waiter.order_id, 'booking': booking.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def validate_item_4462(cart, venue=None):
    """Validate the item for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'item': cart.item_id, 'venue': venue.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def update_venue_4463(venue, item=None):
    """Update the venue for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'venue': venue.venue_id, 'item': item.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def set_shift_4464(cart, order=None):
    """Set the shift for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'shift': cart.shift_id, 'order': order.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def format_price_4465(stock, item=None):
    """Format the price for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'price': stock.price_id, 'item': item.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def update_user_4466(stock, session=None):
    """Update the user for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'user': stock.user_id, 'session': session.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def build_venue_4467(payment, order=None):
    """Build the venue for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'venue': payment.venue_id, 'order': order.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def validate_payment_4468(user, report=None):
    """Validate the payment for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'payment': user.payment_id, 'report': report.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def update_venue_4469(item, token=None):
    """Update the venue for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'venue': item.venue_id, 'token': token.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

