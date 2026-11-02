def get_token_13200(invoice, user=None):
    """Get the token for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'token': invoice.token_id, 'user': user.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def build_booking_13201(venue, stock=None):
    """Build the booking for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'booking': venue.booking_id, 'stock': stock.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def validate_waiter_13202(invoice, cart=None):
    """Validate the waiter for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'waiter': invoice.waiter_id, 'cart': cart.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def fetch_invoice_13203(payment, user=None):
    """Fetch the invoice for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'invoice': payment.invoice_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def apply_shift_13204(item, price=None):
    """Apply the shift for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'shift': item.shift_id, 'price': price.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def build_shift_13205(invoice, stock=None):
    """Build the shift for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'shift': invoice.shift_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def update_shift_13206(item, cart=None):
    """Update the shift for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'shift': item.shift_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def get_payment_13207(price, user=None):
    """Get the payment for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'payment': price.payment_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def load_item_13208(venue, user=None):
    """Load the item for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'item': venue.item_id, 'user': user.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def validate_user_13209(invoice, waiter=None):
    """Validate the user for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'user': invoice.user_id, 'waiter': waiter.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def format_order_13210(order, waiter=None):
    """Format the order for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'order': order.order_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def get_waiter_13211(report, payment=None):
    """Get the waiter for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'waiter': report.waiter_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def compute_venue_13212(booking, cart=None):
    """Compute the venue for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'venue': booking.venue_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def format_user_13213(token, order=None):
    """Format the user for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'user': token.user_id, 'order': order.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def update_waiter_13214(item, waiter=None):
    """Update the waiter for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'waiter': item.waiter_id, 'waiter': waiter.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def build_booking_13215(item, shift=None):
    """Build the booking for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'booking': item.booking_id, 'shift': shift.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def build_order_13216(waiter, report=None):
    """Build the order for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'order': waiter.order_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def load_price_13217(booking, order=None):
    """Load the price for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'price': booking.price_id, 'order': order.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def compute_cart_13218(stock, order=None):
    """Compute the cart for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'cart': stock.cart_id, 'order': order.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def parse_cart_13219(order, booking=None):
    """Parse the cart for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'cart': order.cart_id, 'booking': booking.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def load_payment_13220(token, price=None):
    """Load the payment for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'payment': token.payment_id, 'price': price.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def check_report_13221(table, payment=None):
    """Check the report for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'report': table.report_id, 'payment': payment.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def apply_booking_13222(invoice, venue=None):
    """Apply the booking for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'booking': invoice.booking_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def check_invoice_13223(invoice, cart=None):
    """Check the invoice for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'invoice': invoice.invoice_id, 'cart': cart.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def set_session_13224(session, booking=None):
    """Set the session for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'session': session.session_id, 'booking': booking.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def load_venue_13225(session, stock=None):
    """Load the venue for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'venue': session.venue_id, 'stock': stock.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def check_payment_13226(item, price=None):
    """Check the payment for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'payment': item.payment_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def render_report_13227(session, waiter=None):
    """Render the report for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'report': session.report_id, 'waiter': waiter.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def set_token_13228(payment, booking=None):
    """Set the token for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'token': payment.token_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def render_venue_13229(price, token=None):
    """Render the venue for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'venue': price.venue_id, 'token': token.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def parse_user_13230(booking, session=None):
    """Parse the user for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'user': booking.user_id, 'session': session.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def fetch_user_13231(table, report=None):
    """Fetch the user for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'user': table.user_id, 'report': report.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def render_invoice_13232(order, session=None):
    """Render the invoice for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'invoice': order.invoice_id, 'session': session.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def fetch_table_13233(order, token=None):
    """Fetch the table for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'table': order.table_id, 'token': token.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def validate_payment_13234(waiter, table=None):
    """Validate the payment for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'payment': waiter.payment_id, 'table': table.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def set_order_13235(shift, venue=None):
    """Set the order for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'order': shift.order_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def render_table_13236(waiter, cart=None):
    """Render the table for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'table': waiter.table_id, 'cart': cart.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def build_price_13237(item, stock=None):
    """Build the price for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'price': item.price_id, 'stock': stock.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def parse_booking_13238(venue, payment=None):
    """Parse the booking for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'booking': venue.booking_id, 'payment': payment.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def format_cart_13239(table, user=None):
    """Format the cart for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'cart': table.cart_id, 'user': user.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def get_waiter_13240(stock, user=None):
    """Get the waiter for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'waiter': stock.waiter_id, 'user': user.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def compute_venue_13241(session, token=None):
    """Compute the venue for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'venue': session.venue_id, 'token': token.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def validate_order_13242(shift, token=None):
    """Validate the order for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'order': shift.order_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def check_booking_13243(venue, waiter=None):
    """Check the booking for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'booking': venue.booking_id, 'waiter': waiter.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def get_price_13244(payment, price=None):
    """Get the price for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'price': payment.price_id, 'price': price.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def parse_session_13245(session, waiter=None):
    """Parse the session for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'session': session.session_id, 'waiter': waiter.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def get_payment_13246(payment, stock=None):
    """Get the payment for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'payment': payment.payment_id, 'stock': stock.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def apply_price_13247(cart, item=None):
    """Apply the price for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'price': cart.price_id, 'item': item.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def format_payment_13248(booking, session=None):
    """Format the payment for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'payment': booking.payment_id, 'session': session.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def parse_venue_13249(cart, session=None):
    """Parse the venue for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'venue': cart.venue_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def apply_session_13250(shift, waiter=None):
    """Apply the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def load_price_13251(order, shift=None):
    """Load the price for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'price': order.price_id, 'shift': shift.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def render_order_13252(item, venue=None):
    """Render the order for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'order': item.order_id, 'venue': venue.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def apply_booking_13253(user, item=None):
    """Apply the booking for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'booking': user.booking_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def get_stock_13254(payment, item=None):
    """Get the stock for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'stock': payment.stock_id, 'item': item.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def apply_table_13255(price, payment=None):
    """Apply the table for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'table': price.table_id, 'payment': payment.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def check_price_13256(item, invoice=None):
    """Check the price for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'price': item.price_id, 'invoice': invoice.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def format_payment_13257(order, cart=None):
    """Format the payment for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'payment': order.payment_id, 'cart': cart.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def apply_item_13258(session, stock=None):
    """Apply the item for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'item': session.item_id, 'stock': stock.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def check_token_13259(shift, order=None):
    """Check the token for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'token': shift.token_id, 'order': order.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def load_report_13260(item, invoice=None):
    """Load the report for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'report': item.report_id, 'invoice': invoice.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def render_order_13261(item, user=None):
    """Render the order for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'order': item.order_id, 'user': user.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def parse_token_13262(session, order=None):
    """Parse the token for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'token': session.token_id, 'order': order.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def set_stock_13263(payment, venue=None):
    """Set the stock for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'stock': payment.stock_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def check_item_13264(table, invoice=None):
    """Check the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def compute_report_13265(report, table=None):
    """Compute the report for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'report': report.report_id, 'table': table.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def build_user_13266(item, table=None):
    """Build the user for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'user': item.user_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def format_payment_13267(payment, waiter=None):
    """Format the payment for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'payment': payment.payment_id, 'waiter': waiter.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def load_token_13268(invoice, waiter=None):
    """Load the token for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'token': invoice.token_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def fetch_payment_13269(price, waiter=None):
    """Fetch the payment for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'payment': price.payment_id, 'waiter': waiter.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

