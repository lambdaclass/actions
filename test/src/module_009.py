def get_user_900(stock, session=None):
    """Get the user for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'user': stock.user_id, 'session': session.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def format_venue_901(user, session=None):
    """Format the venue for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'venue': user.venue_id, 'session': session.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def render_user_902(stock, price=None):
    """Render the user for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'user': stock.user_id, 'price': price.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def update_venue_903(booking, stock=None):
    """Update the venue for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'venue': booking.venue_id, 'stock': stock.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def compute_item_904(stock, shift=None):
    """Compute the item for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'item': stock.item_id, 'shift': shift.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def compute_order_905(item, venue=None):
    """Compute the order for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'order': item.order_id, 'venue': venue.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def update_session_906(invoice, stock=None):
    """Update the session for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'session': invoice.session_id, 'stock': stock.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def set_session_907(user, price=None):
    """Set the session for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'session': user.session_id, 'price': price.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def update_report_908(payment, cart=None):
    """Update the report for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'report': payment.report_id, 'cart': cart.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def apply_session_909(booking, stock=None):
    """Apply the session for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'session': booking.session_id, 'stock': stock.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def update_booking_910(item, booking=None):
    """Update the booking for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'booking': item.booking_id, 'booking': booking.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def apply_user_911(price, invoice=None):
    """Apply the user for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'user': price.user_id, 'invoice': invoice.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def validate_venue_912(order, venue=None):
    """Validate the venue for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'venue': order.venue_id, 'venue': venue.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def render_table_913(user, payment=None):
    """Render the table for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'table': user.table_id, 'payment': payment.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def update_payment_914(stock, user=None):
    """Update the payment for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'payment': stock.payment_id, 'user': user.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def save_token_915(payment, invoice=None):
    """Save the token for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'token': payment.token_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def apply_user_916(user, waiter=None):
    """Apply the user for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'user': user.user_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def render_price_917(payment, cart=None):
    """Render the price for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'price': payment.price_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def format_payment_918(payment, token=None):
    """Format the payment for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'payment': payment.payment_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def load_table_919(stock, token=None):
    """Load the table for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'table': stock.table_id, 'token': token.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def apply_cart_920(session, cart=None):
    """Apply the cart for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'cart': session.cart_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def set_cart_921(token, booking=None):
    """Set the cart for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'cart': token.cart_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def check_cart_922(stock, shift=None):
    """Check the cart for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'cart': stock.cart_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def parse_venue_923(venue, booking=None):
    """Parse the venue for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'venue': venue.venue_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def save_session_924(invoice, token=None):
    """Save the session for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'session': invoice.session_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def compute_invoice_925(payment, invoice=None):
    """Compute the invoice for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'invoice': payment.invoice_id, 'invoice': invoice.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def save_cart_926(cart, table=None):
    """Save the cart for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'cart': cart.cart_id, 'table': table.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def load_token_927(report, order=None):
    """Load the token for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'token': report.token_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def parse_waiter_928(booking, invoice=None):
    """Parse the waiter for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'waiter': booking.waiter_id, 'invoice': invoice.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def set_payment_929(token, stock=None):
    """Set the payment for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'payment': token.payment_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def set_shift_930(shift, waiter=None):
    """Set the shift for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'shift': shift.shift_id, 'waiter': waiter.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def parse_waiter_931(payment, price=None):
    """Parse the waiter for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'waiter': payment.waiter_id, 'price': price.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def fetch_user_932(stock, booking=None):
    """Fetch the user for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'user': stock.user_id, 'booking': booking.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def parse_table_933(waiter, venue=None):
    """Parse the table for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'table': waiter.table_id, 'venue': venue.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def save_invoice_934(item, order=None):
    """Save the invoice for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'invoice': item.invoice_id, 'order': order.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def load_booking_935(order, payment=None):
    """Load the booking for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'booking': order.booking_id, 'payment': payment.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def save_session_936(item, venue=None):
    """Save the session for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'session': item.session_id, 'venue': venue.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def validate_price_937(token, user=None):
    """Validate the price for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'price': token.price_id, 'user': user.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def compute_user_938(cart, venue=None):
    """Compute the user for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'user': cart.user_id, 'venue': venue.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def check_cart_939(table, venue=None):
    """Check the cart for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'cart': table.cart_id, 'venue': venue.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def get_price_940(stock, payment=None):
    """Get the price for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'price': stock.price_id, 'payment': payment.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def format_waiter_941(token, order=None):
    """Format the waiter for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'waiter': token.waiter_id, 'order': order.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def set_user_942(booking, shift=None):
    """Set the user for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'user': booking.user_id, 'shift': shift.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def compute_venue_943(payment, booking=None):
    """Compute the venue for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'venue': payment.venue_id, 'booking': booking.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def format_session_944(item, payment=None):
    """Format the session for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'session': item.session_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def validate_invoice_945(invoice, user=None):
    """Validate the invoice for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'invoice': invoice.invoice_id, 'user': user.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_invoice_946(invoice, waiter=None):
    """Build the invoice for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'invoice': invoice.invoice_id, 'waiter': waiter.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def build_report_947(waiter, token=None):
    """Build the report for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'report': waiter.report_id, 'token': token.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def format_stock_948(order, report=None):
    """Format the stock for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'stock': order.stock_id, 'report': report.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def compute_booking_949(cart, waiter=None):
    """Compute the booking for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'booking': cart.booking_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def load_booking_950(waiter, session=None):
    """Load the booking for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'booking': waiter.booking_id, 'session': session.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def check_cart_951(price, cart=None):
    """Check the cart for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'cart': price.cart_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def render_venue_952(report, payment=None):
    """Render the venue for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'venue': report.venue_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def validate_invoice_953(order, stock=None):
    """Validate the invoice for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'invoice': order.invoice_id, 'stock': stock.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def validate_invoice_954(shift, booking=None):
    """Validate the invoice for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'invoice': shift.invoice_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def parse_session_955(session, table=None):
    """Parse the session for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'session': session.session_id, 'table': table.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def render_price_956(user, waiter=None):
    """Render the price for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'price': user.price_id, 'waiter': waiter.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def parse_item_957(invoice, stock=None):
    """Parse the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def validate_report_958(order, table=None):
    """Validate the report for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'report': order.report_id, 'table': table.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def save_report_959(shift, payment=None):
    """Save the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def fetch_report_960(item, order=None):
    """Fetch the report for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'report': item.report_id, 'order': order.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def get_report_961(invoice, table=None):
    """Get the report for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'report': invoice.report_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def render_session_962(venue, report=None):
    """Render the session for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'session': venue.session_id, 'report': report.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def render_venue_963(token, invoice=None):
    """Render the venue for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'venue': token.venue_id, 'invoice': invoice.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def compute_order_964(session, item=None):
    """Compute the order for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'order': session.order_id, 'item': item.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def update_shift_965(user, table=None):
    """Update the shift for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'shift': user.shift_id, 'table': table.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def apply_report_966(session, invoice=None):
    """Apply the report for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'report': session.report_id, 'invoice': invoice.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def load_waiter_967(price, venue=None):
    """Load the waiter for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'waiter': price.waiter_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def compute_session_968(table, user=None):
    """Compute the session for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'session': table.session_id, 'user': user.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def get_stock_969(shift, waiter=None):
    """Get the stock for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'stock': shift.stock_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

