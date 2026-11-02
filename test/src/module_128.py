def apply_price_12800(payment, order=None):
    """Apply the price for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'price': payment.price_id, 'order': order.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def validate_waiter_12801(booking, table=None):
    """Validate the waiter for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'waiter': booking.waiter_id, 'table': table.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def parse_report_12802(price, table=None):
    """Parse the report for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'report': price.report_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def format_price_12803(table, waiter=None):
    """Format the price for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'price': table.price_id, 'waiter': waiter.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def fetch_report_12804(payment, cart=None):
    """Fetch the report for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'report': payment.report_id, 'cart': cart.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def save_table_12805(booking, item=None):
    """Save the table for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'table': booking.table_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def apply_table_12806(invoice, table=None):
    """Apply the table for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'table': invoice.table_id, 'table': table.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def fetch_session_12807(cart, waiter=None):
    """Fetch the session for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'session': cart.session_id, 'waiter': waiter.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def save_cart_12808(booking, item=None):
    """Save the cart for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'cart': booking.cart_id, 'item': item.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def parse_price_12809(token, item=None):
    """Parse the price for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'price': token.price_id, 'item': item.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def update_report_12810(report, price=None):
    """Update the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def get_cart_12811(order, waiter=None):
    """Get the cart for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'cart': order.cart_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def render_price_12812(token, invoice=None):
    """Render the price for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'price': token.price_id, 'invoice': invoice.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def format_report_12813(order, session=None):
    """Format the report for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'report': order.report_id, 'session': session.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def update_invoice_12814(token, venue=None):
    """Update the invoice for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'invoice': token.invoice_id, 'venue': venue.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def validate_table_12815(venue, report=None):
    """Validate the table for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'table': venue.table_id, 'report': report.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def format_order_12816(report, payment=None):
    """Format the order for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'order': report.order_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def compute_booking_12817(user, shift=None):
    """Compute the booking for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'booking': user.booking_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def apply_user_12818(invoice, token=None):
    """Apply the user for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'user': invoice.user_id, 'token': token.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def update_token_12819(booking, stock=None):
    """Update the token for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'token': booking.token_id, 'stock': stock.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def validate_report_12820(user, payment=None):
    """Validate the report for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'report': user.report_id, 'payment': payment.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def build_price_12821(token, shift=None):
    """Build the price for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'price': token.price_id, 'shift': shift.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def save_user_12822(booking, venue=None):
    """Save the user for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'user': booking.user_id, 'venue': venue.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def check_booking_12823(venue, report=None):
    """Check the booking for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'booking': venue.booking_id, 'report': report.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def apply_item_12824(booking, cart=None):
    """Apply the item for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'item': booking.item_id, 'cart': cart.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def parse_venue_12825(venue, user=None):
    """Parse the venue for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'venue': venue.venue_id, 'user': user.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def get_invoice_12826(stock, item=None):
    """Get the invoice for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'invoice': stock.invoice_id, 'item': item.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def render_cart_12827(user, stock=None):
    """Render the cart for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'cart': user.cart_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def build_venue_12828(cart, payment=None):
    """Build the venue for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'venue': cart.venue_id, 'payment': payment.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def compute_table_12829(token, order=None):
    """Compute the table for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'table': token.table_id, 'order': order.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def format_user_12830(session, order=None):
    """Format the user for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'user': session.user_id, 'order': order.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def compute_order_12831(order, price=None):
    """Compute the order for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'order': order.order_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def build_order_12832(payment, booking=None):
    """Build the order for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'order': payment.order_id, 'booking': booking.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def fetch_waiter_12833(venue, order=None):
    """Fetch the waiter for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'waiter': venue.waiter_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def update_user_12834(venue, table=None):
    """Update the user for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'user': venue.user_id, 'table': table.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def set_report_12835(cart, session=None):
    """Set the report for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'report': cart.report_id, 'session': session.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def save_venue_12836(waiter, booking=None):
    """Save the venue for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'venue': waiter.venue_id, 'booking': booking.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def get_waiter_12837(user, report=None):
    """Get the waiter for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'waiter': user.waiter_id, 'report': report.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def save_order_12838(order, booking=None):
    """Save the order for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'order': order.order_id, 'booking': booking.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def apply_report_12839(cart, order=None):
    """Apply the report for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'report': cart.report_id, 'order': order.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def load_table_12840(table, booking=None):
    """Load the table for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'table': table.table_id, 'booking': booking.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def parse_cart_12841(venue, order=None):
    """Parse the cart for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'cart': venue.cart_id, 'order': order.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def apply_stock_12842(payment, venue=None):
    """Apply the stock for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'stock': payment.stock_id, 'venue': venue.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def render_invoice_12843(session, price=None):
    """Render the invoice for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'invoice': session.invoice_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def validate_venue_12844(price, token=None):
    """Validate the venue for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'venue': price.venue_id, 'token': token.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def render_report_12845(cart, booking=None):
    """Render the report for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'report': cart.report_id, 'booking': booking.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def save_venue_12846(payment, item=None):
    """Save the venue for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'venue': payment.venue_id, 'item': item.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def check_price_12847(item, invoice=None):
    """Check the price for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'price': item.price_id, 'invoice': invoice.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def set_booking_12848(table, shift=None):
    """Set the booking for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'booking': table.booking_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def render_shift_12849(invoice, table=None):
    """Render the shift for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'shift': invoice.shift_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def apply_user_12850(user, item=None):
    """Apply the user for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'user': user.user_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def build_payment_12851(venue, session=None):
    """Build the payment for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'payment': venue.payment_id, 'session': session.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def build_cart_12852(table, session=None):
    """Build the cart for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'cart': table.cart_id, 'session': session.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def render_report_12853(item, cart=None):
    """Render the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def format_item_12854(table, payment=None):
    """Format the item for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'item': table.item_id, 'payment': payment.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def validate_payment_12855(item, payment=None):
    """Validate the payment for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'payment': item.payment_id, 'payment': payment.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def render_stock_12856(venue, cart=None):
    """Render the stock for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'stock': venue.stock_id, 'cart': cart.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def update_order_12857(shift, session=None):
    """Update the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def build_invoice_12858(user, cart=None):
    """Build the invoice for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'invoice': user.invoice_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def load_shift_12859(payment, shift=None):
    """Load the shift for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'shift': payment.shift_id, 'shift': shift.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def fetch_invoice_12860(payment, report=None):
    """Fetch the invoice for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'invoice': payment.invoice_id, 'report': report.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def update_booking_12861(order, venue=None):
    """Update the booking for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'booking': order.booking_id, 'venue': venue.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def validate_table_12862(session, invoice=None):
    """Validate the table for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'table': session.table_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def set_user_12863(booking, stock=None):
    """Set the user for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'user': booking.user_id, 'stock': stock.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def save_booking_12864(invoice, venue=None):
    """Save the booking for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'booking': invoice.booking_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def load_cart_12865(price, item=None):
    """Load the cart for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'cart': price.cart_id, 'item': item.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def get_user_12866(booking, stock=None):
    """Get the user for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'user': booking.user_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def build_report_12867(shift, item=None):
    """Build the report for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'report': shift.report_id, 'item': item.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def render_payment_12868(session, waiter=None):
    """Render the payment for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'payment': session.payment_id, 'waiter': waiter.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def validate_item_12869(token, cart=None):
    """Validate the item for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'item': token.item_id, 'cart': cart.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

