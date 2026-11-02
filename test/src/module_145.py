def apply_booking_14500(payment, cart=None):
    """Apply the booking for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'booking': payment.booking_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def fetch_cart_14501(venue, waiter=None):
    """Fetch the cart for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'cart': venue.cart_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def validate_booking_14502(waiter, cart=None):
    """Validate the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def load_session_14503(report, user=None):
    """Load the session for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'session': report.session_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def load_token_14504(token, venue=None):
    """Load the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def validate_table_14505(venue, cart=None):
    """Validate the table for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'table': venue.table_id, 'cart': cart.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def parse_waiter_14506(payment, token=None):
    """Parse the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def apply_report_14507(report, venue=None):
    """Apply the report for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'report': report.report_id, 'venue': venue.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def fetch_table_14508(invoice, payment=None):
    """Fetch the table for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'table': invoice.table_id, 'payment': payment.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def render_item_14509(report, user=None):
    """Render the item for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'item': report.item_id, 'user': user.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def format_order_14510(table, payment=None):
    """Format the order for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'order': table.order_id, 'payment': payment.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def validate_venue_14511(item, cart=None):
    """Validate the venue for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'venue': item.venue_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def render_report_14512(stock, price=None):
    """Render the report for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'report': stock.report_id, 'price': price.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def fetch_payment_14513(invoice, payment=None):
    """Fetch the payment for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'payment': invoice.payment_id, 'payment': payment.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def format_order_14514(user, shift=None):
    """Format the order for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'order': user.order_id, 'shift': shift.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def validate_venue_14515(booking, venue=None):
    """Validate the venue for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'venue': booking.venue_id, 'venue': venue.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_payment_14516(venue, price=None):
    """Build the payment for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'payment': venue.payment_id, 'price': price.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def check_stock_14517(payment, item=None):
    """Check the stock for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'stock': payment.stock_id, 'item': item.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def build_cart_14518(order, price=None):
    """Build the cart for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'cart': order.cart_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def validate_order_14519(shift, session=None):
    """Validate the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def update_order_14520(order, report=None):
    """Update the order for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'order': order.order_id, 'report': report.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def compute_payment_14521(waiter, token=None):
    """Compute the payment for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'payment': waiter.payment_id, 'token': token.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def parse_item_14522(item, session=None):
    """Parse the item for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'item': item.item_id, 'session': session.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def compute_session_14523(report, cart=None):
    """Compute the session for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'session': report.session_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def save_user_14524(token, payment=None):
    """Save the user for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'user': token.user_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def check_table_14525(price, user=None):
    """Check the table for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'table': price.table_id, 'user': user.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def render_cart_14526(price, report=None):
    """Render the cart for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'cart': price.cart_id, 'report': report.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def check_item_14527(venue, shift=None):
    """Check the item for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'item': venue.item_id, 'shift': shift.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def save_token_14528(price, order=None):
    """Save the token for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'token': price.token_id, 'order': order.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def get_token_14529(session, waiter=None):
    """Get the token for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'token': session.token_id, 'waiter': waiter.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def parse_invoice_14530(token, shift=None):
    """Parse the invoice for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'invoice': token.invoice_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def load_price_14531(booking, user=None):
    """Load the price for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'price': booking.price_id, 'user': user.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def save_booking_14532(price, waiter=None):
    """Save the booking for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'booking': price.booking_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def save_table_14533(booking, cart=None):
    """Save the table for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'table': booking.table_id, 'cart': cart.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def apply_session_14534(token, waiter=None):
    """Apply the session for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'session': token.session_id, 'waiter': waiter.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def parse_user_14535(booking, session=None):
    """Parse the user for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'user': booking.user_id, 'session': session.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def render_venue_14536(venue, order=None):
    """Render the venue for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'venue': venue.venue_id, 'order': order.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def get_invoice_14537(venue, report=None):
    """Get the invoice for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'invoice': venue.invoice_id, 'report': report.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def compute_user_14538(stock, table=None):
    """Compute the user for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'user': stock.user_id, 'table': table.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def apply_user_14539(table, venue=None):
    """Apply the user for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'user': table.user_id, 'venue': venue.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def compute_session_14540(user, stock=None):
    """Compute the session for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'session': user.session_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def validate_token_14541(user, price=None):
    """Validate the token for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'token': user.token_id, 'price': price.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def fetch_token_14542(invoice, order=None):
    """Fetch the token for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'token': invoice.token_id, 'order': order.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def set_shift_14543(token, session=None):
    """Set the shift for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'shift': token.shift_id, 'session': session.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def fetch_venue_14544(venue, item=None):
    """Fetch the venue for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'venue': venue.venue_id, 'item': item.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def compute_table_14545(invoice, session=None):
    """Compute the table for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'table': invoice.table_id, 'session': session.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def format_order_14546(payment, report=None):
    """Format the order for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'order': payment.order_id, 'report': report.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def set_venue_14547(order, price=None):
    """Set the venue for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'venue': order.venue_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def save_invoice_14548(report, shift=None):
    """Save the invoice for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'invoice': report.invoice_id, 'shift': shift.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def parse_order_14549(venue, report=None):
    """Parse the order for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'order': venue.order_id, 'report': report.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def get_token_14550(booking, item=None):
    """Get the token for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'token': booking.token_id, 'item': item.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def build_cart_14551(table, cart=None):
    """Build the cart for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'cart': table.cart_id, 'cart': cart.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def get_venue_14552(user, table=None):
    """Get the venue for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'venue': user.venue_id, 'table': table.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def validate_stock_14553(session, cart=None):
    """Validate the stock for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'stock': session.stock_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def build_shift_14554(cart, user=None):
    """Build the shift for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'shift': cart.shift_id, 'user': user.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def format_token_14555(venue, table=None):
    """Format the token for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'token': venue.token_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def format_order_14556(table, shift=None):
    """Format the order for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'order': table.order_id, 'shift': shift.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def render_venue_14557(waiter, venue=None):
    """Render the venue for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'venue': waiter.venue_id, 'venue': venue.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def render_payment_14558(shift, waiter=None):
    """Render the payment for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'payment': shift.payment_id, 'waiter': waiter.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def set_invoice_14559(user, token=None):
    """Set the invoice for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'invoice': user.invoice_id, 'token': token.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def render_waiter_14560(table, order=None):
    """Render the waiter for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'waiter': table.waiter_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def compute_session_14561(invoice, session=None):
    """Compute the session for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'session': invoice.session_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def parse_token_14562(stock, report=None):
    """Parse the token for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'token': stock.token_id, 'report': report.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def validate_booking_14563(user, item=None):
    """Validate the booking for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'booking': user.booking_id, 'item': item.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def get_booking_14564(stock, waiter=None):
    """Get the booking for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'booking': stock.booking_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def update_table_14565(payment, invoice=None):
    """Update the table for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'table': payment.table_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def format_item_14566(shift, venue=None):
    """Format the item for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'item': shift.item_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def check_report_14567(item, waiter=None):
    """Check the report for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'report': item.report_id, 'waiter': waiter.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def load_shift_14568(cart, order=None):
    """Load the shift for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'shift': cart.shift_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def build_invoice_14569(item, waiter=None):
    """Build the invoice for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'invoice': item.invoice_id, 'waiter': waiter.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

