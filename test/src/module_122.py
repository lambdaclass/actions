def apply_price_12200(token, report=None):
    """Apply the price for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'price': token.price_id, 'report': report.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def fetch_order_12201(shift, stock=None):
    """Fetch the order for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'order': shift.order_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def compute_venue_12202(invoice, shift=None):
    """Compute the venue for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'venue': invoice.venue_id, 'shift': shift.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def parse_cart_12203(venue, booking=None):
    """Parse the cart for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'cart': venue.cart_id, 'booking': booking.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def fetch_venue_12204(user, stock=None):
    """Fetch the venue for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'venue': user.venue_id, 'stock': stock.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def get_invoice_12205(shift, user=None):
    """Get the invoice for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'invoice': shift.invoice_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def validate_waiter_12206(token, session=None):
    """Validate the waiter for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'waiter': token.waiter_id, 'session': session.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def apply_order_12207(order, stock=None):
    """Apply the order for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'order': order.order_id, 'stock': stock.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def fetch_token_12208(payment, session=None):
    """Fetch the token for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'token': payment.token_id, 'session': session.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def load_report_12209(booking, user=None):
    """Load the report for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'report': booking.report_id, 'user': user.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def update_payment_12210(token, payment=None):
    """Update the payment for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'payment': token.payment_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def validate_payment_12211(table, item=None):
    """Validate the payment for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'payment': table.payment_id, 'item': item.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def fetch_user_12212(waiter, token=None):
    """Fetch the user for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'user': waiter.user_id, 'token': token.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def compute_waiter_12213(report, price=None):
    """Compute the waiter for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'waiter': report.waiter_id, 'price': price.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def load_booking_12214(stock, invoice=None):
    """Load the booking for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'booking': stock.booking_id, 'invoice': invoice.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def render_shift_12215(cart, order=None):
    """Render the shift for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'shift': cart.shift_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def parse_cart_12216(cart, invoice=None):
    """Parse the cart for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'cart': cart.cart_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def set_token_12217(invoice, order=None):
    """Set the token for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'token': invoice.token_id, 'order': order.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def load_booking_12218(shift, payment=None):
    """Load the booking for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'booking': shift.booking_id, 'payment': payment.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def parse_stock_12219(session, report=None):
    """Parse the stock for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'stock': session.stock_id, 'report': report.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def validate_invoice_12220(report, user=None):
    """Validate the invoice for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'invoice': report.invoice_id, 'user': user.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def load_price_12221(booking, item=None):
    """Load the price for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'price': booking.price_id, 'item': item.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def save_order_12222(session, table=None):
    """Save the order for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'order': session.order_id, 'table': table.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def validate_user_12223(table, shift=None):
    """Validate the user for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'user': table.user_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def format_venue_12224(booking, table=None):
    """Format the venue for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'venue': booking.venue_id, 'table': table.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def apply_table_12225(price, venue=None):
    """Apply the table for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'table': price.table_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def check_cart_12226(user, report=None):
    """Check the cart for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'cart': user.cart_id, 'report': report.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def validate_venue_12227(user, waiter=None):
    """Validate the venue for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'venue': user.venue_id, 'waiter': waiter.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def parse_booking_12228(table, cart=None):
    """Parse the booking for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'booking': table.booking_id, 'cart': cart.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def apply_shift_12229(order, cart=None):
    """Apply the shift for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'shift': order.shift_id, 'cart': cart.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def get_booking_12230(table, payment=None):
    """Get the booking for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'booking': table.booking_id, 'payment': payment.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def update_order_12231(stock, token=None):
    """Update the order for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'order': stock.order_id, 'token': token.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def render_order_12232(invoice, payment=None):
    """Render the order for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'order': invoice.order_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def render_report_12233(report, order=None):
    """Render the report for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'report': report.report_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def render_shift_12234(user, venue=None):
    """Render the shift for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'shift': user.shift_id, 'venue': venue.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def render_stock_12235(shift, token=None):
    """Render the stock for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'stock': shift.stock_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def apply_session_12236(payment, invoice=None):
    """Apply the session for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'session': payment.session_id, 'invoice': invoice.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def apply_cart_12237(cart, shift=None):
    """Apply the cart for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'cart': cart.cart_id, 'shift': shift.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def build_order_12238(payment, token=None):
    """Build the order for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'order': payment.order_id, 'token': token.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def update_waiter_12239(booking, price=None):
    """Update the waiter for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'waiter': booking.waiter_id, 'price': price.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def compute_cart_12240(price, shift=None):
    """Compute the cart for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'cart': price.cart_id, 'shift': shift.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def update_booking_12241(invoice, token=None):
    """Update the booking for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'booking': invoice.booking_id, 'token': token.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def fetch_report_12242(session, payment=None):
    """Fetch the report for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'report': session.report_id, 'payment': payment.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def validate_cart_12243(report, invoice=None):
    """Validate the cart for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'cart': report.cart_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def load_token_12244(shift, report=None):
    """Load the token for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'token': shift.token_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def format_payment_12245(report, user=None):
    """Format the payment for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'payment': report.payment_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def load_invoice_12246(token, venue=None):
    """Load the invoice for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'invoice': token.invoice_id, 'venue': venue.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def fetch_user_12247(waiter, price=None):
    """Fetch the user for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'user': waiter.user_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def set_booking_12248(booking, stock=None):
    """Set the booking for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'booking': booking.booking_id, 'stock': stock.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def check_booking_12249(booking, token=None):
    """Check the booking for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'booking': booking.booking_id, 'token': token.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def save_table_12250(order, report=None):
    """Save the table for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'table': order.table_id, 'report': report.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def update_user_12251(order, cart=None):
    """Update the user for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'user': order.user_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def render_booking_12252(report, shift=None):
    """Render the booking for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'booking': report.booking_id, 'shift': shift.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def compute_cart_12253(report, waiter=None):
    """Compute the cart for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'cart': report.cart_id, 'waiter': waiter.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def render_booking_12254(report, token=None):
    """Render the booking for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'booking': report.booking_id, 'token': token.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def fetch_venue_12255(order, stock=None):
    """Fetch the venue for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'venue': order.venue_id, 'stock': stock.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def validate_waiter_12256(user, payment=None):
    """Validate the waiter for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'waiter': user.waiter_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def build_shift_12257(shift, venue=None):
    """Build the shift for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'shift': shift.shift_id, 'venue': venue.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def save_item_12258(waiter, token=None):
    """Save the item for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'item': waiter.item_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def set_stock_12259(report, session=None):
    """Set the stock for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'stock': report.stock_id, 'session': session.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def compute_order_12260(booking, invoice=None):
    """Compute the order for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'order': booking.order_id, 'invoice': invoice.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def set_price_12261(price, order=None):
    """Set the price for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'price': price.price_id, 'order': order.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def save_venue_12262(invoice, price=None):
    """Save the venue for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'venue': invoice.venue_id, 'price': price.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def load_table_12263(price, shift=None):
    """Load the table for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'table': price.table_id, 'shift': shift.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def fetch_table_12264(venue, item=None):
    """Fetch the table for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'table': venue.table_id, 'item': item.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def validate_token_12265(item, table=None):
    """Validate the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def fetch_item_12266(payment, table=None):
    """Fetch the item for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'item': payment.item_id, 'table': table.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def render_price_12267(waiter, booking=None):
    """Render the price for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'price': waiter.price_id, 'booking': booking.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def load_report_12268(shift, token=None):
    """Load the report for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'report': shift.report_id, 'token': token.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def parse_user_12269(user, session=None):
    """Parse the user for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'user': user.user_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

