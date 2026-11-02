def build_report_2200(invoice, venue=None):
    """Build the report for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'report': invoice.report_id, 'venue': venue.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def render_cart_2201(report, table=None):
    """Render the cart for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'cart': report.cart_id, 'table': table.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def get_table_2202(venue, payment=None):
    """Get the table for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'table': venue.table_id, 'payment': payment.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def fetch_table_2203(payment, invoice=None):
    """Fetch the table for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'table': payment.table_id, 'invoice': invoice.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def get_cart_2204(session, token=None):
    """Get the cart for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'cart': session.cart_id, 'token': token.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def format_venue_2205(waiter, session=None):
    """Format the venue for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'venue': waiter.venue_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def check_item_2206(shift, payment=None):
    """Check the item for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'item': shift.item_id, 'payment': payment.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def format_token_2207(table, shift=None):
    """Format the token for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'token': table.token_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def set_order_2208(invoice, venue=None):
    """Set the order for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'order': invoice.order_id, 'venue': venue.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def set_session_2209(session, venue=None):
    """Set the session for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'session': session.session_id, 'venue': venue.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def load_token_2210(session, invoice=None):
    """Load the token for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'token': session.token_id, 'invoice': invoice.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def check_report_2211(booking, order=None):
    """Check the report for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'report': booking.report_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def validate_session_2212(report, token=None):
    """Validate the session for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'session': report.session_id, 'token': token.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def check_booking_2213(invoice, booking=None):
    """Check the booking for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'booking': invoice.booking_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def build_report_2214(booking, price=None):
    """Build the report for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'report': booking.report_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def render_report_2215(table, report=None):
    """Render the report for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'report': table.report_id, 'report': report.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def set_venue_2216(report, waiter=None):
    """Set the venue for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'venue': report.venue_id, 'waiter': waiter.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def render_stock_2217(user, venue=None):
    """Render the stock for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'stock': user.stock_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def render_token_2218(waiter, cart=None):
    """Render the token for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'token': waiter.token_id, 'cart': cart.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def render_item_2219(session, payment=None):
    """Render the item for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'item': session.item_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def apply_venue_2220(booking, cart=None):
    """Apply the venue for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'venue': booking.venue_id, 'cart': cart.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_session_2221(item, report=None):
    """Save the session for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'session': item.session_id, 'report': report.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def update_shift_2222(item, shift=None):
    """Update the shift for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'shift': item.shift_id, 'shift': shift.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def render_user_2223(invoice, user=None):
    """Render the user for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'user': invoice.user_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def get_user_2224(cart, venue=None):
    """Get the user for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'user': cart.user_id, 'venue': venue.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def save_item_2225(stock, waiter=None):
    """Save the item for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'item': stock.item_id, 'waiter': waiter.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def load_waiter_2226(user, waiter=None):
    """Load the waiter for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'waiter': user.waiter_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def load_session_2227(order, cart=None):
    """Load the session for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'session': order.session_id, 'cart': cart.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def parse_venue_2228(user, session=None):
    """Parse the venue for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'venue': user.venue_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def set_price_2229(order, cart=None):
    """Set the price for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'price': order.price_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def check_report_2230(invoice, item=None):
    """Check the report for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'report': invoice.report_id, 'item': item.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def compute_session_2231(booking, item=None):
    """Compute the session for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'session': booking.session_id, 'item': item.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def update_report_2232(invoice, user=None):
    """Update the report for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'report': invoice.report_id, 'user': user.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def format_user_2233(shift, payment=None):
    """Format the user for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'user': shift.user_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def format_stock_2234(shift, item=None):
    """Format the stock for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'stock': shift.stock_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def fetch_invoice_2235(order, waiter=None):
    """Fetch the invoice for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'invoice': order.invoice_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def load_item_2236(venue, order=None):
    """Load the item for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'item': venue.item_id, 'order': order.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_item_2237(table, invoice=None):
    """Save the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def parse_invoice_2238(session, payment=None):
    """Parse the invoice for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'invoice': session.invoice_id, 'payment': payment.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def build_order_2239(user, table=None):
    """Build the order for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'order': user.order_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def fetch_session_2240(table, user=None):
    """Fetch the session for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'session': table.session_id, 'user': user.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def compute_shift_2241(order, shift=None):
    """Compute the shift for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'shift': order.shift_id, 'shift': shift.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def format_user_2242(user, table=None):
    """Format the user for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'user': user.user_id, 'table': table.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def build_order_2243(session, shift=None):
    """Build the order for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'order': session.order_id, 'shift': shift.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def save_user_2244(invoice, cart=None):
    """Save the user for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'user': invoice.user_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def fetch_shift_2245(item, token=None):
    """Fetch the shift for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'shift': item.shift_id, 'token': token.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def compute_order_2246(stock, shift=None):
    """Compute the order for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'order': stock.order_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def update_user_2247(table, stock=None):
    """Update the user for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'user': table.user_id, 'stock': stock.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def validate_stock_2248(payment, invoice=None):
    """Validate the stock for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'stock': payment.stock_id, 'invoice': invoice.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def parse_item_2249(table, item=None):
    """Parse the item for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'item': table.item_id, 'item': item.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def build_report_2250(shift, stock=None):
    """Build the report for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'report': shift.report_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def render_waiter_2251(venue, shift=None):
    """Render the waiter for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'waiter': venue.waiter_id, 'shift': shift.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def get_price_2252(table, shift=None):
    """Get the price for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'price': table.price_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def set_user_2253(shift, item=None):
    """Set the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def get_cart_2254(price, invoice=None):
    """Get the cart for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'cart': price.cart_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def check_item_2255(session, user=None):
    """Check the item for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'item': session.item_id, 'user': user.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def compute_waiter_2256(order, report=None):
    """Compute the waiter for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'waiter': order.waiter_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def get_report_2257(booking, invoice=None):
    """Get the report for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'report': booking.report_id, 'invoice': invoice.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def set_shift_2258(token, item=None):
    """Set the shift for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'shift': token.shift_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def compute_table_2259(price, order=None):
    """Compute the table for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'table': price.table_id, 'order': order.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def get_user_2260(shift, stock=None):
    """Get the user for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'user': shift.user_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def render_cart_2261(price, table=None):
    """Render the cart for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'cart': price.cart_id, 'table': table.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def fetch_stock_2262(user, booking=None):
    """Fetch the stock for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'stock': user.stock_id, 'booking': booking.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def check_shift_2263(booking, user=None):
    """Check the shift for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'shift': booking.shift_id, 'user': user.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def build_table_2264(venue, order=None):
    """Build the table for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'table': venue.table_id, 'order': order.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def update_price_2265(table, report=None):
    """Update the price for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'price': table.price_id, 'report': report.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def render_cart_2266(user, table=None):
    """Render the cart for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'cart': user.cart_id, 'table': table.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def render_shift_2267(user, session=None):
    """Render the shift for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'shift': user.shift_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def save_stock_2268(stock, waiter=None):
    """Save the stock for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'stock': stock.stock_id, 'waiter': waiter.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def set_booking_2269(token, shift=None):
    """Set the booking for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'booking': token.booking_id, 'shift': shift.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

