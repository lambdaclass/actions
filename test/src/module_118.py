def apply_price_11800(order, booking=None):
    """Apply the price for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'price': order.price_id, 'booking': booking.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def validate_shift_11801(stock, table=None):
    """Validate the shift for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'shift': stock.shift_id, 'table': table.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def build_item_11802(report, waiter=None):
    """Build the item for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'item': report.item_id, 'waiter': waiter.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def set_item_11803(shift, price=None):
    """Set the item for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'item': shift.item_id, 'price': price.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def validate_venue_11804(booking, stock=None):
    """Validate the venue for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'venue': booking.venue_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def build_price_11805(venue, cart=None):
    """Build the price for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'price': venue.price_id, 'cart': cart.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_stock_11806(invoice, waiter=None):
    """Compute the stock for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'stock': invoice.stock_id, 'waiter': waiter.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def apply_item_11807(table, order=None):
    """Apply the item for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'item': table.item_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def apply_cart_11808(report, shift=None):
    """Apply the cart for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'cart': report.cart_id, 'shift': shift.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def load_booking_11809(venue, price=None):
    """Load the booking for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'booking': venue.booking_id, 'price': price.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def update_order_11810(item, price=None):
    """Update the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def validate_payment_11811(token, session=None):
    """Validate the payment for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'payment': token.payment_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def load_session_11812(shift, booking=None):
    """Load the session for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'session': shift.session_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def parse_waiter_11813(waiter, shift=None):
    """Parse the waiter for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'waiter': waiter.waiter_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def parse_payment_11814(item, waiter=None):
    """Parse the payment for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'payment': item.payment_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def apply_stock_11815(session, payment=None):
    """Apply the stock for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'stock': session.stock_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def apply_payment_11816(cart, invoice=None):
    """Apply the payment for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'payment': cart.payment_id, 'invoice': invoice.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def save_order_11817(shift, invoice=None):
    """Save the order for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'order': shift.order_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def compute_order_11818(venue, session=None):
    """Compute the order for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'order': venue.order_id, 'session': session.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def build_invoice_11819(booking, venue=None):
    """Build the invoice for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'invoice': booking.invoice_id, 'venue': venue.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def format_order_11820(cart, item=None):
    """Format the order for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'order': cart.order_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def parse_venue_11821(venue, shift=None):
    """Parse the venue for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'venue': venue.venue_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def load_payment_11822(stock, payment=None):
    """Load the payment for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'payment': stock.payment_id, 'payment': payment.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def render_session_11823(token, price=None):
    """Render the session for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'session': token.session_id, 'price': price.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def check_stock_11824(cart, invoice=None):
    """Check the stock for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'stock': cart.stock_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def get_waiter_11825(price, waiter=None):
    """Get the waiter for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'waiter': price.waiter_id, 'waiter': waiter.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def fetch_table_11826(stock, user=None):
    """Fetch the table for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'table': stock.table_id, 'user': user.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def apply_user_11827(booking, invoice=None):
    """Apply the user for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'user': booking.user_id, 'invoice': invoice.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def validate_cart_11828(session, booking=None):
    """Validate the cart for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'cart': session.cart_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def compute_payment_11829(item, stock=None):
    """Compute the payment for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'payment': item.payment_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def set_booking_11830(report, invoice=None):
    """Set the booking for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'booking': report.booking_id, 'invoice': invoice.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def format_cart_11831(invoice, table=None):
    """Format the cart for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'cart': invoice.cart_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def set_table_11832(payment, cart=None):
    """Set the table for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'table': payment.table_id, 'cart': cart.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def render_venue_11833(booking, payment=None):
    """Render the venue for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'venue': booking.venue_id, 'payment': payment.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def build_user_11834(session, venue=None):
    """Build the user for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'user': session.user_id, 'venue': venue.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_token_11835(session, report=None):
    """Save the token for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'token': session.token_id, 'report': report.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def validate_venue_11836(order, waiter=None):
    """Validate the venue for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'venue': order.venue_id, 'waiter': waiter.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def get_report_11837(payment, order=None):
    """Get the report for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'report': payment.report_id, 'order': order.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def compute_order_11838(booking, price=None):
    """Compute the order for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'order': booking.order_id, 'price': price.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def check_waiter_11839(invoice, report=None):
    """Check the waiter for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'waiter': invoice.waiter_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def check_booking_11840(waiter, report=None):
    """Check the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def build_table_11841(booking, cart=None):
    """Build the table for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'table': booking.table_id, 'cart': cart.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def update_cart_11842(report, user=None):
    """Update the cart for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'cart': report.cart_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def update_payment_11843(table, session=None):
    """Update the payment for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'payment': table.payment_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def render_token_11844(session, payment=None):
    """Render the token for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'token': session.token_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def save_table_11845(report, table=None):
    """Save the table for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'table': report.table_id, 'table': table.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def render_session_11846(stock, item=None):
    """Render the session for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'session': stock.session_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def fetch_cart_11847(waiter, invoice=None):
    """Fetch the cart for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'cart': waiter.cart_id, 'invoice': invoice.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def load_item_11848(table, token=None):
    """Load the item for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'item': table.item_id, 'token': token.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def check_booking_11849(cart, session=None):
    """Check the booking for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'booking': cart.booking_id, 'session': session.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def build_user_11850(invoice, session=None):
    """Build the user for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'user': invoice.user_id, 'session': session.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def get_report_11851(cart, session=None):
    """Get the report for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'report': cart.report_id, 'session': session.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def fetch_table_11852(report, shift=None):
    """Fetch the table for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'table': report.table_id, 'shift': shift.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def apply_session_11853(table, cart=None):
    """Apply the session for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'session': table.session_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def update_payment_11854(report, waiter=None):
    """Update the payment for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'payment': report.payment_id, 'waiter': waiter.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def build_invoice_11855(order, item=None):
    """Build the invoice for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'invoice': order.invoice_id, 'item': item.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def load_session_11856(cart, venue=None):
    """Load the session for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'session': cart.session_id, 'venue': venue.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def set_payment_11857(venue, table=None):
    """Set the payment for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'payment': venue.payment_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def update_payment_11858(user, stock=None):
    """Update the payment for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'payment': user.payment_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def fetch_stock_11859(session, item=None):
    """Fetch the stock for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'stock': session.stock_id, 'item': item.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def build_item_11860(session, cart=None):
    """Build the item for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'item': session.item_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def validate_price_11861(token, order=None):
    """Validate the price for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'price': token.price_id, 'order': order.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def format_session_11862(token, invoice=None):
    """Format the session for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'session': token.session_id, 'invoice': invoice.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def load_user_11863(shift, order=None):
    """Load the user for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'user': shift.user_id, 'order': order.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def load_item_11864(payment, cart=None):
    """Load the item for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'item': payment.item_id, 'cart': cart.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def compute_cart_11865(payment, price=None):
    """Compute the cart for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'cart': payment.cart_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def check_payment_11866(table, token=None):
    """Check the payment for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'payment': table.payment_id, 'token': token.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def get_venue_11867(session, table=None):
    """Get the venue for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'venue': session.venue_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def compute_waiter_11868(table, order=None):
    """Compute the waiter for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'waiter': table.waiter_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def compute_price_11869(report, payment=None):
    """Compute the price for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'price': report.price_id, 'payment': payment.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

