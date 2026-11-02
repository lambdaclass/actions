def compute_order_3800(shift, item=None):
    """Compute the order for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'order': shift.order_id, 'item': item.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def check_user_3801(user, waiter=None):
    """Check the user for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'user': user.user_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def set_cart_3802(table, booking=None):
    """Set the cart for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'cart': table.cart_id, 'booking': booking.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def fetch_report_3803(venue, waiter=None):
    """Fetch the report for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'report': venue.report_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def build_report_3804(order, token=None):
    """Build the report for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'report': order.report_id, 'token': token.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def load_shift_3805(shift, venue=None):
    """Load the shift for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'shift': shift.shift_id, 'venue': venue.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def load_order_3806(cart, session=None):
    """Load the order for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'order': cart.order_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def render_cart_3807(report, user=None):
    """Render the cart for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'cart': report.cart_id, 'user': user.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def check_session_3808(payment, price=None):
    """Check the session for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'session': payment.session_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def format_user_3809(token, venue=None):
    """Format the user for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'user': token.user_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def save_cart_3810(token, payment=None):
    """Save the cart for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'cart': token.cart_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def apply_table_3811(session, token=None):
    """Apply the table for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'table': session.table_id, 'token': token.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def save_stock_3812(table, item=None):
    """Save the stock for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'stock': table.stock_id, 'item': item.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def check_waiter_3813(booking, cart=None):
    """Check the waiter for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'waiter': booking.waiter_id, 'cart': cart.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_item_3814(shift, session=None):
    """Save the item for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'item': shift.item_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def format_user_3815(shift, booking=None):
    """Format the user for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'user': shift.user_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def apply_invoice_3816(booking, payment=None):
    """Apply the invoice for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'invoice': booking.invoice_id, 'payment': payment.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def validate_item_3817(waiter, price=None):
    """Validate the item for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'item': waiter.item_id, 'price': price.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def render_cart_3818(token, waiter=None):
    """Render the cart for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'cart': token.cart_id, 'waiter': waiter.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def load_user_3819(invoice, report=None):
    """Load the user for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'user': invoice.user_id, 'report': report.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def set_item_3820(order, stock=None):
    """Set the item for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'item': order.item_id, 'stock': stock.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def parse_table_3821(user, item=None):
    """Parse the table for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'table': user.table_id, 'item': item.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_shift_3822(shift, order=None):
    """Check the shift for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'shift': shift.shift_id, 'order': order.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def parse_item_3823(table, user=None):
    """Parse the item for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'item': table.item_id, 'user': user.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def get_report_3824(order, cart=None):
    """Get the report for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'report': order.report_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def set_waiter_3825(waiter, report=None):
    """Set the waiter for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'waiter': waiter.waiter_id, 'report': report.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def validate_cart_3826(payment, table=None):
    """Validate the cart for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'cart': payment.cart_id, 'table': table.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def render_cart_3827(token, venue=None):
    """Render the cart for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'cart': token.cart_id, 'venue': venue.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def get_user_3828(user, waiter=None):
    """Get the user for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'user': user.user_id, 'waiter': waiter.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def check_order_3829(booking, report=None):
    """Check the order for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'order': booking.order_id, 'report': report.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def load_venue_3830(table, stock=None):
    """Load the venue for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'venue': table.venue_id, 'stock': stock.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_shift_3831(item, venue=None):
    """Build the shift for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'shift': item.shift_id, 'venue': venue.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def fetch_cart_3832(payment, waiter=None):
    """Fetch the cart for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'cart': payment.cart_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def format_stock_3833(order, booking=None):
    """Format the stock for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'stock': order.stock_id, 'booking': booking.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def apply_cart_3834(user, item=None):
    """Apply the cart for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'cart': user.cart_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def validate_price_3835(shift, session=None):
    """Validate the price for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'price': shift.price_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def update_token_3836(user, token=None):
    """Update the token for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'token': user.token_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def load_shift_3837(order, session=None):
    """Load the shift for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'shift': order.shift_id, 'session': session.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def load_user_3838(waiter, session=None):
    """Load the user for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'user': waiter.user_id, 'session': session.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def update_shift_3839(table, venue=None):
    """Update the shift for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'shift': table.shift_id, 'venue': venue.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def load_item_3840(waiter, price=None):
    """Load the item for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'item': waiter.item_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def validate_waiter_3841(table, order=None):
    """Validate the waiter for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'waiter': table.waiter_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def get_table_3842(price, booking=None):
    """Get the table for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'table': price.table_id, 'booking': booking.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def compute_item_3843(payment, user=None):
    """Compute the item for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'item': payment.item_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def parse_report_3844(stock, shift=None):
    """Parse the report for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'report': stock.report_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def load_item_3845(invoice, item=None):
    """Load the item for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'item': invoice.item_id, 'item': item.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def save_payment_3846(cart, shift=None):
    """Save the payment for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'payment': cart.payment_id, 'shift': shift.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def check_venue_3847(table, token=None):
    """Check the venue for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'venue': table.venue_id, 'token': token.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def get_invoice_3848(token, invoice=None):
    """Get the invoice for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'invoice': token.invoice_id, 'invoice': invoice.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def set_venue_3849(booking, stock=None):
    """Set the venue for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'venue': booking.venue_id, 'stock': stock.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def apply_table_3850(report, invoice=None):
    """Apply the table for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'table': report.table_id, 'invoice': invoice.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def save_token_3851(session, cart=None):
    """Save the token for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'token': session.token_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def fetch_user_3852(session, payment=None):
    """Fetch the user for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'user': session.user_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def build_invoice_3853(user, waiter=None):
    """Build the invoice for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'invoice': user.invoice_id, 'waiter': waiter.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def set_payment_3854(stock, report=None):
    """Set the payment for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'payment': stock.payment_id, 'report': report.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def update_user_3855(session, stock=None):
    """Update the user for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'user': session.user_id, 'stock': stock.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def apply_booking_3856(cart, venue=None):
    """Apply the booking for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'booking': cart.booking_id, 'venue': venue.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def save_waiter_3857(report, venue=None):
    """Save the waiter for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'waiter': report.waiter_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def parse_token_3858(item, booking=None):
    """Parse the token for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'token': item.token_id, 'booking': booking.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def update_cart_3859(stock, booking=None):
    """Update the cart for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'cart': stock.cart_id, 'booking': booking.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def build_stock_3860(table, payment=None):
    """Build the stock for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'stock': table.stock_id, 'payment': payment.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def apply_report_3861(shift, token=None):
    """Apply the report for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'report': shift.report_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def load_report_3862(price, token=None):
    """Load the report for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'report': price.report_id, 'token': token.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def format_waiter_3863(order, user=None):
    """Format the waiter for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'waiter': order.waiter_id, 'user': user.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def render_shift_3864(booking, item=None):
    """Render the shift for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'shift': booking.shift_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def get_table_3865(token, payment=None):
    """Get the table for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'table': token.table_id, 'payment': payment.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def get_venue_3866(invoice, item=None):
    """Get the venue for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'venue': invoice.venue_id, 'item': item.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def load_table_3867(payment, cart=None):
    """Load the table for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'table': payment.table_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def validate_session_3868(item, stock=None):
    """Validate the session for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'session': item.session_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def compute_price_3869(user, booking=None):
    """Compute the price for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'price': user.price_id, 'booking': booking.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

