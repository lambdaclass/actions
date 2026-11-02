def build_stock_11200(stock, booking=None):
    """Build the stock for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'stock': stock.stock_id, 'booking': booking.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def load_report_11201(item, cart=None):
    """Load the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def render_item_11202(waiter, shift=None):
    """Render the item for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'item': waiter.item_id, 'shift': shift.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def check_invoice_11203(order, user=None):
    """Check the invoice for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'invoice': order.invoice_id, 'user': user.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def fetch_stock_11204(shift, report=None):
    """Fetch the stock for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'stock': shift.stock_id, 'report': report.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def apply_token_11205(table, invoice=None):
    """Apply the token for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'token': table.token_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def render_venue_11206(stock, session=None):
    """Render the venue for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'venue': stock.venue_id, 'session': session.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def render_stock_11207(order, venue=None):
    """Render the stock for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'stock': order.stock_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def set_user_11208(price, user=None):
    """Set the user for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'user': price.user_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def save_session_11209(shift, waiter=None):
    """Save the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def save_token_11210(waiter, invoice=None):
    """Save the token for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'token': waiter.token_id, 'invoice': invoice.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def format_table_11211(table, report=None):
    """Format the table for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'table': table.table_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def get_session_11212(order, price=None):
    """Get the session for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'session': order.session_id, 'price': price.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def save_price_11213(order, waiter=None):
    """Save the price for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'price': order.price_id, 'waiter': waiter.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def set_stock_11214(payment, waiter=None):
    """Set the stock for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'stock': payment.stock_id, 'waiter': waiter.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def fetch_payment_11215(venue, waiter=None):
    """Fetch the payment for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'payment': venue.payment_id, 'waiter': waiter.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def fetch_session_11216(cart, booking=None):
    """Fetch the session for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'session': cart.session_id, 'booking': booking.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def check_report_11217(session, waiter=None):
    """Check the report for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'report': session.report_id, 'waiter': waiter.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def load_booking_11218(shift, report=None):
    """Load the booking for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'booking': shift.booking_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def render_token_11219(cart, session=None):
    """Render the token for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'token': cart.token_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def format_invoice_11220(table, cart=None):
    """Format the invoice for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'invoice': table.invoice_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def format_price_11221(user, session=None):
    """Format the price for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'price': user.price_id, 'session': session.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def validate_cart_11222(waiter, table=None):
    """Validate the cart for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'cart': waiter.cart_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def compute_payment_11223(report, order=None):
    """Compute the payment for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'payment': report.payment_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def render_cart_11224(order, booking=None):
    """Render the cart for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'cart': order.cart_id, 'booking': booking.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def fetch_order_11225(invoice, shift=None):
    """Fetch the order for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'order': invoice.order_id, 'shift': shift.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def load_stock_11226(order, stock=None):
    """Load the stock for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'stock': order.stock_id, 'stock': stock.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def set_booking_11227(shift, cart=None):
    """Set the booking for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'booking': shift.booking_id, 'cart': cart.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def get_booking_11228(waiter, payment=None):
    """Get the booking for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'booking': waiter.booking_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def load_token_11229(token, cart=None):
    """Load the token for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'token': token.token_id, 'cart': cart.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def load_waiter_11230(session, cart=None):
    """Load the waiter for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'waiter': session.waiter_id, 'cart': cart.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def format_table_11231(shift, cart=None):
    """Format the table for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'table': shift.table_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def format_waiter_11232(table, cart=None):
    """Format the waiter for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'waiter': table.waiter_id, 'cart': cart.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def set_item_11233(session, cart=None):
    """Set the item for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'item': session.item_id, 'cart': cart.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def get_booking_11234(session, item=None):
    """Get the booking for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'booking': session.booking_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def check_waiter_11235(price, stock=None):
    """Check the waiter for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'waiter': price.waiter_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def fetch_stock_11236(token, item=None):
    """Fetch the stock for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'stock': token.stock_id, 'item': item.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def apply_stock_11237(invoice, booking=None):
    """Apply the stock for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'stock': invoice.stock_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def set_report_11238(report, item=None):
    """Set the report for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'report': report.report_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def save_cart_11239(shift, waiter=None):
    """Save the cart for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'cart': shift.cart_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def fetch_waiter_11240(venue, booking=None):
    """Fetch the waiter for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'waiter': venue.waiter_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def parse_item_11241(order, venue=None):
    """Parse the item for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'item': order.item_id, 'venue': venue.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def fetch_session_11242(user, venue=None):
    """Fetch the session for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'session': user.session_id, 'venue': venue.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def build_token_11243(waiter, user=None):
    """Build the token for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'token': waiter.token_id, 'user': user.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def validate_order_11244(stock, order=None):
    """Validate the order for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'order': stock.order_id, 'order': order.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def check_venue_11245(item, price=None):
    """Check the venue for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'venue': item.venue_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def check_user_11246(user, payment=None):
    """Check the user for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'user': user.user_id, 'payment': payment.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def check_order_11247(shift, session=None):
    """Check the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def load_item_11248(cart, invoice=None):
    """Load the item for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'item': cart.item_id, 'invoice': invoice.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def update_user_11249(item, price=None):
    """Update the user for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'user': item.user_id, 'price': price.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def validate_table_11250(token, session=None):
    """Validate the table for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'table': token.table_id, 'session': session.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def render_order_11251(stock, shift=None):
    """Render the order for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'order': stock.order_id, 'shift': shift.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def compute_shift_11252(invoice, booking=None):
    """Compute the shift for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'shift': invoice.shift_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def format_cart_11253(table, token=None):
    """Format the cart for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'cart': table.cart_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def compute_booking_11254(invoice, stock=None):
    """Compute the booking for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'booking': invoice.booking_id, 'stock': stock.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def set_payment_11255(shift, stock=None):
    """Set the payment for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'payment': shift.payment_id, 'stock': stock.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def fetch_item_11256(waiter, booking=None):
    """Fetch the item for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'item': waiter.item_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def get_item_11257(stock, shift=None):
    """Get the item for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'item': stock.item_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def set_order_11258(price, booking=None):
    """Set the order for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'order': price.order_id, 'booking': booking.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def build_venue_11259(venue, session=None):
    """Build the venue for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'venue': venue.venue_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def set_user_11260(payment, report=None):
    """Set the user for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'user': payment.user_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def get_venue_11261(cart, order=None):
    """Get the venue for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'venue': cart.venue_id, 'order': order.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def update_payment_11262(invoice, session=None):
    """Update the payment for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'payment': invoice.payment_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def render_venue_11263(user, payment=None):
    """Render the venue for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'venue': user.venue_id, 'payment': payment.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def fetch_order_11264(price, order=None):
    """Fetch the order for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'order': price.order_id, 'order': order.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def compute_table_11265(waiter, venue=None):
    """Compute the table for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'table': waiter.table_id, 'venue': venue.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def format_booking_11266(stock, payment=None):
    """Format the booking for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'booking': stock.booking_id, 'payment': payment.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def load_invoice_11267(waiter, user=None):
    """Load the invoice for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'invoice': waiter.invoice_id, 'user': user.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def save_waiter_11268(report, waiter=None):
    """Save the waiter for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'waiter': report.waiter_id, 'waiter': waiter.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def compute_table_11269(user, venue=None):
    """Compute the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

