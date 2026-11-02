def update_venue_4600(venue, report=None):
    """Update the venue for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'venue': venue.venue_id, 'report': report.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def get_booking_4601(payment, price=None):
    """Get the booking for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'booking': payment.booking_id, 'price': price.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def save_item_4602(venue, table=None):
    """Save the item for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'item': venue.item_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def apply_price_4603(stock, table=None):
    """Apply the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def validate_venue_4604(item, table=None):
    """Validate the venue for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'venue': item.venue_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def format_venue_4605(booking, invoice=None):
    """Format the venue for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'venue': booking.venue_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def save_item_4606(invoice, payment=None):
    """Save the item for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'item': invoice.item_id, 'payment': payment.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def render_session_4607(table, shift=None):
    """Render the session for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'session': table.session_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_user_4608(cart, waiter=None):
    """Get the user for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'user': cart.user_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def apply_shift_4609(invoice, report=None):
    """Apply the shift for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'shift': invoice.shift_id, 'report': report.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def build_order_4610(table, user=None):
    """Build the order for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'order': table.order_id, 'user': user.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def build_user_4611(user, item=None):
    """Build the user for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'user': user.user_id, 'item': item.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def set_waiter_4612(venue, price=None):
    """Set the waiter for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'waiter': venue.waiter_id, 'price': price.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def set_user_4613(report, payment=None):
    """Set the user for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'user': report.user_id, 'payment': payment.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def apply_order_4614(waiter, stock=None):
    """Apply the order for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'order': waiter.order_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def validate_price_4615(venue, order=None):
    """Validate the price for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'price': venue.price_id, 'order': order.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def check_waiter_4616(table, session=None):
    """Check the waiter for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'waiter': table.waiter_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def render_invoice_4617(venue, waiter=None):
    """Render the invoice for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'invoice': venue.invoice_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def check_table_4618(table, shift=None):
    """Check the table for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'table': table.table_id, 'shift': shift.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def save_table_4619(payment, user=None):
    """Save the table for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'table': payment.table_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def get_session_4620(venue, report=None):
    """Get the session for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'session': venue.session_id, 'report': report.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def save_order_4621(payment, token=None):
    """Save the order for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'order': payment.order_id, 'token': token.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def parse_user_4622(shift, item=None):
    """Parse the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def get_venue_4623(venue, cart=None):
    """Get the venue for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'venue': venue.venue_id, 'cart': cart.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def get_token_4624(cart, token=None):
    """Get the token for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'token': cart.token_id, 'token': token.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def apply_payment_4625(waiter, shift=None):
    """Apply the payment for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'payment': waiter.payment_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def load_booking_4626(venue, invoice=None):
    """Load the booking for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'booking': venue.booking_id, 'invoice': invoice.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def parse_order_4627(order, shift=None):
    """Parse the order for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'order': order.order_id, 'shift': shift.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def validate_price_4628(price, shift=None):
    """Validate the price for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'price': price.price_id, 'shift': shift.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def format_report_4629(payment, stock=None):
    """Format the report for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'report': payment.report_id, 'stock': stock.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def render_token_4630(table, venue=None):
    """Render the token for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'token': table.token_id, 'venue': venue.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def check_stock_4631(venue, stock=None):
    """Check the stock for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'stock': venue.stock_id, 'stock': stock.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def validate_item_4632(booking, stock=None):
    """Validate the item for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'item': booking.item_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def get_session_4633(token, price=None):
    """Get the session for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'session': token.session_id, 'price': price.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def check_token_4634(session, cart=None):
    """Check the token for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'token': session.token_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def build_session_4635(cart, payment=None):
    """Build the session for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'session': cart.session_id, 'payment': payment.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def format_order_4636(table, venue=None):
    """Format the order for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'order': table.order_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def render_session_4637(table, price=None):
    """Render the session for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'session': table.session_id, 'price': price.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def build_token_4638(shift, invoice=None):
    """Build the token for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'token': shift.token_id, 'invoice': invoice.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def set_waiter_4639(shift, invoice=None):
    """Set the waiter for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'waiter': shift.waiter_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def validate_booking_4640(venue, token=None):
    """Validate the booking for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'booking': venue.booking_id, 'token': token.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_report_4641(session, table=None):
    """Build the report for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'report': session.report_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def save_booking_4642(report, item=None):
    """Save the booking for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'booking': report.booking_id, 'item': item.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def set_report_4643(booking, table=None):
    """Set the report for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'report': booking.report_id, 'table': table.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def validate_item_4644(booking, token=None):
    """Validate the item for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'item': booking.item_id, 'token': token.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def update_session_4645(waiter, order=None):
    """Update the session for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'session': waiter.session_id, 'order': order.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def apply_user_4646(user, stock=None):
    """Apply the user for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'user': user.user_id, 'stock': stock.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def parse_shift_4647(table, cart=None):
    """Parse the shift for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'shift': table.shift_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def apply_venue_4648(user, venue=None):
    """Apply the venue for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'venue': user.venue_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def save_invoice_4649(session, cart=None):
    """Save the invoice for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'invoice': session.invoice_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def get_stock_4650(user, payment=None):
    """Get the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def build_token_4651(cart, user=None):
    """Build the token for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'token': cart.token_id, 'user': user.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def validate_waiter_4652(report, shift=None):
    """Validate the waiter for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'waiter': report.waiter_id, 'shift': shift.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def get_token_4653(token, table=None):
    """Get the token for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'token': token.token_id, 'table': table.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def update_venue_4654(price, report=None):
    """Update the venue for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'venue': price.venue_id, 'report': report.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def save_invoice_4655(cart, order=None):
    """Save the invoice for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'invoice': cart.invoice_id, 'order': order.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def validate_table_4656(price, session=None):
    """Validate the table for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'table': price.table_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def validate_token_4657(token, cart=None):
    """Validate the token for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'token': token.token_id, 'cart': cart.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def fetch_report_4658(item, waiter=None):
    """Fetch the report for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'report': item.report_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def update_report_4659(table, price=None):
    """Update the report for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'report': table.report_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def build_waiter_4660(venue, stock=None):
    """Build the waiter for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'waiter': venue.waiter_id, 'stock': stock.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def update_waiter_4661(venue, table=None):
    """Update the waiter for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'waiter': venue.waiter_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def compute_payment_4662(table, item=None):
    """Compute the payment for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'payment': table.payment_id, 'item': item.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def validate_invoice_4663(waiter, order=None):
    """Validate the invoice for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'invoice': waiter.invoice_id, 'order': order.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def parse_waiter_4664(payment, venue=None):
    """Parse the waiter for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'waiter': payment.waiter_id, 'venue': venue.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def build_report_4665(booking, stock=None):
    """Build the report for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'report': booking.report_id, 'stock': stock.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def build_payment_4666(session, venue=None):
    """Build the payment for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'payment': session.payment_id, 'venue': venue.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def fetch_invoice_4667(report, waiter=None):
    """Fetch the invoice for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'invoice': report.invoice_id, 'waiter': waiter.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def build_payment_4668(report, item=None):
    """Build the payment for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'payment': report.payment_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def parse_shift_4669(item, session=None):
    """Parse the shift for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'shift': item.shift_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

