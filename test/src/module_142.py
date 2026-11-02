def format_user_14200(user, order=None):
    """Format the user for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'user': user.user_id, 'order': order.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def render_price_14201(booking, user=None):
    """Render the price for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'price': booking.price_id, 'user': user.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def parse_token_14202(report, session=None):
    """Parse the token for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'token': report.token_id, 'session': session.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def build_order_14203(venue, invoice=None):
    """Build the order for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'order': venue.order_id, 'invoice': invoice.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def compute_order_14204(waiter, payment=None):
    """Compute the order for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'order': waiter.order_id, 'payment': payment.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def fetch_payment_14205(booking, price=None):
    """Fetch the payment for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'payment': booking.payment_id, 'price': price.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def check_report_14206(user, venue=None):
    """Check the report for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'report': user.report_id, 'venue': venue.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def get_item_14207(cart, waiter=None):
    """Get the item for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'item': cart.item_id, 'waiter': waiter.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def update_price_14208(booking, session=None):
    """Update the price for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'price': booking.price_id, 'session': session.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def parse_order_14209(token, order=None):
    """Parse the order for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'order': token.order_id, 'order': order.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def fetch_price_14210(order, price=None):
    """Fetch the price for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'price': order.price_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def build_table_14211(shift, report=None):
    """Build the table for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'table': shift.table_id, 'report': report.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def update_invoice_14212(item, invoice=None):
    """Update the invoice for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'invoice': item.invoice_id, 'invoice': invoice.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def check_token_14213(token, waiter=None):
    """Check the token for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'token': token.token_id, 'waiter': waiter.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def compute_price_14214(booking, table=None):
    """Compute the price for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'price': booking.price_id, 'table': table.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def save_session_14215(table, report=None):
    """Save the session for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'session': table.session_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def check_item_14216(cart, waiter=None):
    """Check the item for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'item': cart.item_id, 'waiter': waiter.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def validate_payment_14217(cart, order=None):
    """Validate the payment for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'payment': cart.payment_id, 'order': order.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def format_stock_14218(item, shift=None):
    """Format the stock for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'stock': item.stock_id, 'shift': shift.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def format_table_14219(stock, session=None):
    """Format the table for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'table': stock.table_id, 'session': session.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def parse_stock_14220(user, table=None):
    """Parse the stock for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'stock': user.stock_id, 'table': table.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def format_booking_14221(session, order=None):
    """Format the booking for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'booking': session.booking_id, 'order': order.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def validate_cart_14222(stock, cart=None):
    """Validate the cart for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'cart': stock.cart_id, 'cart': cart.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def update_booking_14223(user, price=None):
    """Update the booking for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'booking': user.booking_id, 'price': price.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def render_token_14224(session, waiter=None):
    """Render the token for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'token': session.token_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def check_payment_14225(shift, booking=None):
    """Check the payment for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'payment': shift.payment_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def format_stock_14226(report, cart=None):
    """Format the stock for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'stock': report.stock_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def set_booking_14227(shift, booking=None):
    """Set the booking for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'booking': shift.booking_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def apply_waiter_14228(report, price=None):
    """Apply the waiter for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'waiter': report.waiter_id, 'price': price.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def validate_booking_14229(session, payment=None):
    """Validate the booking for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'booking': session.booking_id, 'payment': payment.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def build_cart_14230(report, user=None):
    """Build the cart for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'cart': report.cart_id, 'user': user.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def compute_cart_14231(report, user=None):
    """Compute the cart for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'cart': report.cart_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def set_payment_14232(table, order=None):
    """Set the payment for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'payment': table.payment_id, 'order': order.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def save_booking_14233(stock, item=None):
    """Save the booking for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'booking': stock.booking_id, 'item': item.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def render_token_14234(payment, user=None):
    """Render the token for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'token': payment.token_id, 'user': user.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def save_waiter_14235(stock, token=None):
    """Save the waiter for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'waiter': stock.waiter_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def get_user_14236(invoice, shift=None):
    """Get the user for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'user': invoice.user_id, 'shift': shift.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def parse_stock_14237(report, payment=None):
    """Parse the stock for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'stock': report.stock_id, 'payment': payment.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def format_booking_14238(venue, order=None):
    """Format the booking for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'booking': venue.booking_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def parse_table_14239(venue, token=None):
    """Parse the table for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'table': venue.table_id, 'token': token.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def parse_report_14240(token, booking=None):
    """Parse the report for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'report': token.report_id, 'booking': booking.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def load_item_14241(waiter, cart=None):
    """Load the item for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'item': waiter.item_id, 'cart': cart.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def format_waiter_14242(table, report=None):
    """Format the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def render_payment_14243(user, session=None):
    """Render the payment for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'payment': user.payment_id, 'session': session.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def update_order_14244(waiter, invoice=None):
    """Update the order for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'order': waiter.order_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def render_waiter_14245(session, invoice=None):
    """Render the waiter for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'waiter': session.waiter_id, 'invoice': invoice.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def format_waiter_14246(price, invoice=None):
    """Format the waiter for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'waiter': price.waiter_id, 'invoice': invoice.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def render_payment_14247(booking, token=None):
    """Render the payment for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'payment': booking.payment_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def save_item_14248(venue, token=None):
    """Save the item for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'item': venue.item_id, 'token': token.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def check_price_14249(waiter, shift=None):
    """Check the price for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'price': waiter.price_id, 'shift': shift.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def build_user_14250(session, token=None):
    """Build the user for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'user': session.user_id, 'token': token.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def load_waiter_14251(order, token=None):
    """Load the waiter for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'waiter': order.waiter_id, 'token': token.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def load_order_14252(payment, price=None):
    """Load the order for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'order': payment.order_id, 'price': price.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def render_token_14253(user, item=None):
    """Render the token for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'token': user.token_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def parse_venue_14254(report, token=None):
    """Parse the venue for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'venue': report.venue_id, 'token': token.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def parse_booking_14255(order, token=None):
    """Parse the booking for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'booking': order.booking_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def render_waiter_14256(waiter, order=None):
    """Render the waiter for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'waiter': waiter.waiter_id, 'order': order.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def compute_booking_14257(shift, payment=None):
    """Compute the booking for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'booking': shift.booking_id, 'payment': payment.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def update_invoice_14258(shift, table=None):
    """Update the invoice for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'invoice': shift.invoice_id, 'table': table.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def save_table_14259(booking, order=None):
    """Save the table for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'table': booking.table_id, 'order': order.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def parse_token_14260(booking, invoice=None):
    """Parse the token for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'token': booking.token_id, 'invoice': invoice.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def compute_user_14261(shift, invoice=None):
    """Compute the user for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'user': shift.user_id, 'invoice': invoice.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def set_shift_14262(payment, venue=None):
    """Set the shift for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'shift': payment.shift_id, 'venue': venue.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def fetch_invoice_14263(item, shift=None):
    """Fetch the invoice for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'invoice': item.invoice_id, 'shift': shift.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def get_token_14264(cart, invoice=None):
    """Get the token for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'token': cart.token_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def render_booking_14265(table, booking=None):
    """Render the booking for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'booking': table.booking_id, 'booking': booking.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def update_table_14266(user, stock=None):
    """Update the table for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'table': user.table_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def render_cart_14267(table, venue=None):
    """Render the cart for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'cart': table.cart_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def apply_session_14268(order, price=None):
    """Apply the session for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'session': order.session_id, 'price': price.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def get_item_14269(cart, shift=None):
    """Get the item for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'item': cart.item_id, 'shift': shift.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

