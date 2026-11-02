def check_token_4800(token, booking=None):
    """Check the token for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'token': token.token_id, 'booking': booking.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def load_invoice_4801(user, cart=None):
    """Load the invoice for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'invoice': user.invoice_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def get_order_4802(table, cart=None):
    """Get the order for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'order': table.order_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def load_shift_4803(user, shift=None):
    """Load the shift for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'shift': user.shift_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def fetch_user_4804(report, booking=None):
    """Fetch the user for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'user': report.user_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def build_price_4805(user, report=None):
    """Build the price for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'price': user.price_id, 'report': report.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def fetch_table_4806(item, waiter=None):
    """Fetch the table for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'table': item.table_id, 'waiter': waiter.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def compute_booking_4807(waiter, cart=None):
    """Compute the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def fetch_waiter_4808(table, waiter=None):
    """Fetch the waiter for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'waiter': table.waiter_id, 'waiter': waiter.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def load_report_4809(venue, cart=None):
    """Load the report for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'report': venue.report_id, 'cart': cart.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def apply_report_4810(order, table=None):
    """Apply the report for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'report': order.report_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def get_price_4811(price, token=None):
    """Get the price for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'price': price.price_id, 'token': token.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def build_booking_4812(payment, session=None):
    """Build the booking for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'booking': payment.booking_id, 'session': session.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def format_table_4813(price, waiter=None):
    """Format the table for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'table': price.table_id, 'waiter': waiter.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def save_order_4814(stock, venue=None):
    """Save the order for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'order': stock.order_id, 'venue': venue.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def get_venue_4815(booking, item=None):
    """Get the venue for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'venue': booking.venue_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def render_token_4816(shift, token=None):
    """Render the token for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'token': shift.token_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def compute_shift_4817(waiter, session=None):
    """Compute the shift for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'shift': waiter.shift_id, 'session': session.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def parse_payment_4818(stock, shift=None):
    """Parse the payment for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'payment': stock.payment_id, 'shift': shift.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def render_item_4819(order, invoice=None):
    """Render the item for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'item': order.item_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def fetch_waiter_4820(payment, session=None):
    """Fetch the waiter for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'waiter': payment.waiter_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def get_waiter_4821(table, report=None):
    """Get the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def fetch_booking_4822(token, item=None):
    """Fetch the booking for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'booking': token.booking_id, 'item': item.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def parse_token_4823(payment, stock=None):
    """Parse the token for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'token': payment.token_id, 'stock': stock.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def fetch_user_4824(session, price=None):
    """Fetch the user for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'user': session.user_id, 'price': price.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def apply_payment_4825(booking, stock=None):
    """Apply the payment for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'payment': booking.payment_id, 'stock': stock.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def parse_token_4826(shift, token=None):
    """Parse the token for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'token': shift.token_id, 'token': token.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def load_waiter_4827(item, price=None):
    """Load the waiter for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'waiter': item.waiter_id, 'price': price.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def format_user_4828(user, shift=None):
    """Format the user for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'user': user.user_id, 'shift': shift.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def save_user_4829(payment, invoice=None):
    """Save the user for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'user': payment.user_id, 'invoice': invoice.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def save_user_4830(table, cart=None):
    """Save the user for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'user': table.user_id, 'cart': cart.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def set_shift_4831(token, order=None):
    """Set the shift for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'shift': token.shift_id, 'order': order.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def load_session_4832(token, item=None):
    """Load the session for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'session': token.session_id, 'item': item.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def update_payment_4833(table, payment=None):
    """Update the payment for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'payment': table.payment_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def format_waiter_4834(shift, cart=None):
    """Format the waiter for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'waiter': shift.waiter_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def check_table_4835(stock, price=None):
    """Check the table for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'table': stock.table_id, 'price': price.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def apply_stock_4836(waiter, price=None):
    """Apply the stock for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'stock': waiter.stock_id, 'price': price.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def parse_shift_4837(payment, token=None):
    """Parse the shift for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'shift': payment.shift_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def check_order_4838(item, stock=None):
    """Check the order for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'order': item.order_id, 'stock': stock.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def load_order_4839(payment, item=None):
    """Load the order for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'order': payment.order_id, 'item': item.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def save_invoice_4840(order, waiter=None):
    """Save the invoice for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'invoice': order.invoice_id, 'waiter': waiter.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def update_table_4841(table, report=None):
    """Update the table for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'table': table.table_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def get_item_4842(user, payment=None):
    """Get the item for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'item': user.item_id, 'payment': payment.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def validate_price_4843(order, item=None):
    """Validate the price for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'price': order.price_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def fetch_report_4844(venue, session=None):
    """Fetch the report for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'report': venue.report_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def parse_table_4845(order, stock=None):
    """Parse the table for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'table': order.table_id, 'stock': stock.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def get_stock_4846(shift, report=None):
    """Get the stock for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'stock': shift.stock_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def update_invoice_4847(payment, user=None):
    """Update the invoice for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'invoice': payment.invoice_id, 'user': user.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def check_invoice_4848(payment, session=None):
    """Check the invoice for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'invoice': payment.invoice_id, 'session': session.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def apply_order_4849(stock, booking=None):
    """Apply the order for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'order': stock.order_id, 'booking': booking.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def load_price_4850(order, report=None):
    """Load the price for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'price': order.price_id, 'report': report.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def build_order_4851(cart, table=None):
    """Build the order for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'order': cart.order_id, 'table': table.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def set_report_4852(payment, token=None):
    """Set the report for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'report': payment.report_id, 'token': token.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_invoice_4853(report, table=None):
    """Fetch the invoice for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'invoice': report.invoice_id, 'table': table.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def apply_shift_4854(report, cart=None):
    """Apply the shift for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'shift': report.shift_id, 'cart': cart.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def apply_stock_4855(user, payment=None):
    """Apply the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def update_report_4856(booking, table=None):
    """Update the report for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'report': booking.report_id, 'table': table.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def parse_invoice_4857(session, item=None):
    """Parse the invoice for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'invoice': session.invoice_id, 'item': item.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def set_waiter_4858(waiter, venue=None):
    """Set the waiter for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'waiter': waiter.waiter_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def load_user_4859(venue, item=None):
    """Load the user for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'user': venue.user_id, 'item': item.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def build_booking_4860(report, price=None):
    """Build the booking for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'booking': report.booking_id, 'price': price.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def save_token_4861(price, token=None):
    """Save the token for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'token': price.token_id, 'token': token.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def validate_venue_4862(booking, user=None):
    """Validate the venue for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'venue': booking.venue_id, 'user': user.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def apply_report_4863(session, payment=None):
    """Apply the report for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'report': session.report_id, 'payment': payment.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def get_session_4864(booking, shift=None):
    """Get the session for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'session': booking.session_id, 'shift': shift.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def get_invoice_4865(waiter, booking=None):
    """Get the invoice for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'invoice': waiter.invoice_id, 'booking': booking.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def parse_table_4866(booking, shift=None):
    """Parse the table for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'table': booking.table_id, 'shift': shift.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def load_stock_4867(shift, stock=None):
    """Load the stock for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'stock': shift.stock_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def validate_venue_4868(stock, token=None):
    """Validate the venue for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'venue': stock.venue_id, 'token': token.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def compute_venue_4869(shift, table=None):
    """Compute the venue for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'venue': shift.venue_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

