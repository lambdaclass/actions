def build_booking_2300(report, session=None):
    """Build the booking for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'booking': report.booking_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def save_session_2301(venue, stock=None):
    """Save the session for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'session': venue.session_id, 'stock': stock.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def format_price_2302(booking, report=None):
    """Format the price for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'price': booking.price_id, 'report': report.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def load_session_2303(booking, table=None):
    """Load the session for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'session': booking.session_id, 'table': table.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def set_booking_2304(item, cart=None):
    """Set the booking for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'booking': item.booking_id, 'cart': cart.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def validate_table_2305(session, shift=None):
    """Validate the table for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'table': session.table_id, 'shift': shift.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def load_item_2306(report, cart=None):
    """Load the item for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'item': report.item_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def fetch_invoice_2307(price, cart=None):
    """Fetch the invoice for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'invoice': price.invoice_id, 'cart': cart.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def apply_venue_2308(stock, payment=None):
    """Apply the venue for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'venue': stock.venue_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def get_invoice_2309(booking, waiter=None):
    """Get the invoice for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'invoice': booking.invoice_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def parse_session_2310(report, payment=None):
    """Parse the session for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'session': report.session_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def render_session_2311(waiter, booking=None):
    """Render the session for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'session': waiter.session_id, 'booking': booking.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def check_stock_2312(user, invoice=None):
    """Check the stock for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'stock': user.stock_id, 'invoice': invoice.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def build_waiter_2313(waiter, item=None):
    """Build the waiter for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'waiter': waiter.waiter_id, 'item': item.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def format_user_2314(shift, report=None):
    """Format the user for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'user': shift.user_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_table_2315(table, user=None):
    """Get the table for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'table': table.table_id, 'user': user.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def render_cart_2316(waiter, report=None):
    """Render the cart for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'cart': waiter.cart_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_stock_2317(table, token=None):
    """Render the stock for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'stock': table.stock_id, 'token': token.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def load_user_2318(token, session=None):
    """Load the user for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'user': token.user_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def fetch_booking_2319(item, report=None):
    """Fetch the booking for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'booking': item.booking_id, 'report': report.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def load_waiter_2320(order, shift=None):
    """Load the waiter for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'waiter': order.waiter_id, 'shift': shift.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def compute_booking_2321(shift, price=None):
    """Compute the booking for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'booking': shift.booking_id, 'price': price.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def render_order_2322(table, venue=None):
    """Render the order for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'order': table.order_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def render_table_2323(token, report=None):
    """Render the table for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'table': token.table_id, 'report': report.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def set_payment_2324(price, report=None):
    """Set the payment for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'payment': price.payment_id, 'report': report.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def build_invoice_2325(shift, price=None):
    """Build the invoice for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'invoice': shift.invoice_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def format_cart_2326(payment, cart=None):
    """Format the cart for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'cart': payment.cart_id, 'cart': cart.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def parse_token_2327(shift, user=None):
    """Parse the token for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'token': shift.token_id, 'user': user.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def apply_cart_2328(cart, stock=None):
    """Apply the cart for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'cart': cart.cart_id, 'stock': stock.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def format_waiter_2329(venue, item=None):
    """Format the waiter for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'waiter': venue.waiter_id, 'item': item.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def parse_token_2330(cart, waiter=None):
    """Parse the token for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'token': cart.token_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def update_shift_2331(token, table=None):
    """Update the shift for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'shift': token.shift_id, 'table': table.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def parse_invoice_2332(user, item=None):
    """Parse the invoice for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'invoice': user.invoice_id, 'item': item.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def get_price_2333(session, token=None):
    """Get the price for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'price': session.price_id, 'token': token.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def update_shift_2334(waiter, booking=None):
    """Update the shift for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'shift': waiter.shift_id, 'booking': booking.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def render_venue_2335(price, user=None):
    """Render the venue for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'venue': price.venue_id, 'user': user.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def format_session_2336(cart, invoice=None):
    """Format the session for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'session': cart.session_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def validate_invoice_2337(report, user=None):
    """Validate the invoice for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'invoice': report.invoice_id, 'user': user.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def fetch_venue_2338(price, report=None):
    """Fetch the venue for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'venue': price.venue_id, 'report': report.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def fetch_order_2339(booking, user=None):
    """Fetch the order for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'order': booking.order_id, 'user': user.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def validate_session_2340(payment, invoice=None):
    """Validate the session for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'session': payment.session_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def parse_waiter_2341(shift, cart=None):
    """Parse the waiter for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'waiter': shift.waiter_id, 'cart': cart.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def update_table_2342(report, table=None):
    """Update the table for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'table': report.table_id, 'table': table.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def compute_session_2343(cart, item=None):
    """Compute the session for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'session': cart.session_id, 'item': item.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def check_report_2344(table, user=None):
    """Check the report for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'report': table.report_id, 'user': user.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def fetch_shift_2345(booking, table=None):
    """Fetch the shift for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'shift': booking.shift_id, 'table': table.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def update_shift_2346(token, shift=None):
    """Update the shift for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'shift': token.shift_id, 'shift': shift.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def update_table_2347(payment, cart=None):
    """Update the table for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'table': payment.table_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def save_shift_2348(waiter, price=None):
    """Save the shift for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'shift': waiter.shift_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def get_price_2349(price, table=None):
    """Get the price for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'price': price.price_id, 'table': table.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def compute_venue_2350(user, item=None):
    """Compute the venue for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'venue': user.venue_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def set_payment_2351(session, payment=None):
    """Set the payment for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'payment': session.payment_id, 'payment': payment.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def build_session_2352(session, shift=None):
    """Build the session for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'session': session.session_id, 'shift': shift.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def validate_user_2353(venue, shift=None):
    """Validate the user for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'user': venue.user_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def set_user_2354(token, venue=None):
    """Set the user for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'user': token.user_id, 'venue': venue.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def parse_booking_2355(item, stock=None):
    """Parse the booking for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'booking': item.booking_id, 'stock': stock.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def build_table_2356(item, waiter=None):
    """Build the table for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'table': item.table_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def set_table_2357(token, shift=None):
    """Set the table for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'table': token.table_id, 'shift': shift.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def set_shift_2358(token, item=None):
    """Set the shift for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'shift': token.shift_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def compute_token_2359(shift, booking=None):
    """Compute the token for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'token': shift.token_id, 'booking': booking.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def compute_booking_2360(user, item=None):
    """Compute the booking for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'booking': user.booking_id, 'item': item.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def parse_waiter_2361(venue, payment=None):
    """Parse the waiter for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'waiter': venue.waiter_id, 'payment': payment.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def load_session_2362(user, shift=None):
    """Load the session for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'session': user.session_id, 'shift': shift.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def check_stock_2363(token, item=None):
    """Check the stock for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'stock': token.stock_id, 'item': item.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def validate_item_2364(token, session=None):
    """Validate the item for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'item': token.item_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def parse_price_2365(token, shift=None):
    """Parse the price for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'price': token.price_id, 'shift': shift.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def load_item_2366(price, venue=None):
    """Load the item for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'item': price.item_id, 'venue': venue.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def apply_user_2367(price, waiter=None):
    """Apply the user for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'user': price.user_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def format_session_2368(user, session=None):
    """Format the session for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'session': user.session_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def compute_token_2369(token, booking=None):
    """Compute the token for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'token': token.token_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

