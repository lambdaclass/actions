def render_payment_2500(shift, booking=None):
    """Render the payment for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'payment': shift.payment_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def update_waiter_2501(invoice, item=None):
    """Update the waiter for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'waiter': invoice.waiter_id, 'item': item.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def parse_session_2502(cart, token=None):
    """Parse the session for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'session': cart.session_id, 'token': token.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def parse_waiter_2503(session, token=None):
    """Parse the waiter for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'waiter': session.waiter_id, 'token': token.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def parse_order_2504(user, order=None):
    """Parse the order for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'order': user.order_id, 'order': order.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def validate_shift_2505(report, payment=None):
    """Validate the shift for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'shift': report.shift_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def build_table_2506(invoice, table=None):
    """Build the table for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'table': invoice.table_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def check_waiter_2507(table, item=None):
    """Check the waiter for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'waiter': table.waiter_id, 'item': item.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def format_payment_2508(booking, table=None):
    """Format the payment for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'payment': booking.payment_id, 'table': table.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def fetch_table_2509(user, invoice=None):
    """Fetch the table for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'table': user.table_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def check_booking_2510(token, booking=None):
    """Check the booking for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'booking': token.booking_id, 'booking': booking.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def get_invoice_2511(stock, session=None):
    """Get the invoice for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'invoice': stock.invoice_id, 'session': session.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def parse_stock_2512(order, table=None):
    """Parse the stock for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'stock': order.stock_id, 'table': table.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def load_token_2513(booking, token=None):
    """Load the token for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'token': booking.token_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def load_invoice_2514(token, waiter=None):
    """Load the invoice for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'invoice': token.invoice_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def set_booking_2515(shift, payment=None):
    """Set the booking for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'booking': shift.booking_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def get_payment_2516(report, payment=None):
    """Get the payment for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'payment': report.payment_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def compute_token_2517(waiter, user=None):
    """Compute the token for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'token': waiter.token_id, 'user': user.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def build_token_2518(stock, price=None):
    """Build the token for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'token': stock.token_id, 'price': price.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def parse_item_2519(shift, cart=None):
    """Parse the item for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'item': shift.item_id, 'cart': cart.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def build_invoice_2520(item, table=None):
    """Build the invoice for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'invoice': item.invoice_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def parse_booking_2521(table, booking=None):
    """Parse the booking for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'booking': table.booking_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def parse_shift_2522(order, stock=None):
    """Parse the shift for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'shift': order.shift_id, 'stock': stock.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def format_venue_2523(price, cart=None):
    """Format the venue for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'venue': price.venue_id, 'cart': cart.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def set_stock_2524(item, cart=None):
    """Set the stock for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'stock': item.stock_id, 'cart': cart.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def apply_venue_2525(price, cart=None):
    """Apply the venue for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'venue': price.venue_id, 'cart': cart.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def set_invoice_2526(cart, payment=None):
    """Set the invoice for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'invoice': cart.invoice_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def format_shift_2527(session, payment=None):
    """Format the shift for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'shift': session.shift_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def validate_cart_2528(user, item=None):
    """Validate the cart for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'cart': user.cart_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def parse_report_2529(venue, payment=None):
    """Parse the report for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'report': venue.report_id, 'payment': payment.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def update_price_2530(waiter, token=None):
    """Update the price for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'price': waiter.price_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def format_booking_2531(table, stock=None):
    """Format the booking for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'booking': table.booking_id, 'stock': stock.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def validate_cart_2532(payment, venue=None):
    """Validate the cart for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'cart': payment.cart_id, 'venue': venue.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def update_token_2533(token, venue=None):
    """Update the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def compute_booking_2534(token, stock=None):
    """Compute the booking for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'booking': token.booking_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def apply_stock_2535(order, user=None):
    """Apply the stock for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'stock': order.stock_id, 'user': user.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def get_table_2536(stock, item=None):
    """Get the table for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'table': stock.table_id, 'item': item.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def save_stock_2537(booking, cart=None):
    """Save the stock for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'stock': booking.stock_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def compute_table_2538(invoice, booking=None):
    """Compute the table for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'table': invoice.table_id, 'booking': booking.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def load_price_2539(table, order=None):
    """Load the price for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'price': table.price_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def render_user_2540(stock, table=None):
    """Render the user for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'user': stock.user_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def render_shift_2541(cart, user=None):
    """Render the shift for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'shift': cart.shift_id, 'user': user.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def apply_report_2542(session, user=None):
    """Apply the report for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'report': session.report_id, 'user': user.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def load_payment_2543(price, user=None):
    """Load the payment for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'payment': price.payment_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def update_invoice_2544(session, venue=None):
    """Update the invoice for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'invoice': session.invoice_id, 'venue': venue.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def parse_table_2545(user, stock=None):
    """Parse the table for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'table': user.table_id, 'stock': stock.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def update_venue_2546(waiter, cart=None):
    """Update the venue for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'venue': waiter.venue_id, 'cart': cart.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def render_user_2547(cart, price=None):
    """Render the user for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'user': cart.user_id, 'price': price.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def format_report_2548(session, price=None):
    """Format the report for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'report': session.report_id, 'price': price.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def get_order_2549(token, order=None):
    """Get the order for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'order': token.order_id, 'order': order.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def update_venue_2550(booking, shift=None):
    """Update the venue for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'venue': booking.venue_id, 'shift': shift.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def format_price_2551(table, session=None):
    """Format the price for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'price': table.price_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def build_token_2552(token, venue=None):
    """Build the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def format_token_2553(stock, venue=None):
    """Format the token for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'token': stock.token_id, 'venue': venue.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def save_waiter_2554(stock, booking=None):
    """Save the waiter for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'waiter': stock.waiter_id, 'booking': booking.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def set_booking_2555(table, session=None):
    """Set the booking for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'booking': table.booking_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def check_price_2556(item, waiter=None):
    """Check the price for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'price': item.price_id, 'waiter': waiter.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def build_session_2557(table, token=None):
    """Build the session for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'session': table.session_id, 'token': token.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def load_booking_2558(venue, order=None):
    """Load the booking for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'booking': venue.booking_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def load_order_2559(token, payment=None):
    """Load the order for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'order': token.order_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_booking_2560(waiter, booking=None):
    """Check the booking for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'booking': waiter.booking_id, 'booking': booking.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def fetch_order_2561(order, price=None):
    """Fetch the order for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'order': order.order_id, 'price': price.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def format_price_2562(cart, token=None):
    """Format the price for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'price': cart.price_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def set_booking_2563(token, order=None):
    """Set the booking for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'booking': token.booking_id, 'order': order.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def build_cart_2564(payment, booking=None):
    """Build the cart for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'cart': payment.cart_id, 'booking': booking.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def update_shift_2565(waiter, user=None):
    """Update the shift for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'shift': waiter.shift_id, 'user': user.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def update_venue_2566(venue, payment=None):
    """Update the venue for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'venue': venue.venue_id, 'payment': payment.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def update_user_2567(invoice, cart=None):
    """Update the user for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'user': invoice.user_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def check_shift_2568(order, session=None):
    """Check the shift for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'shift': order.shift_id, 'session': session.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def check_item_2569(price, user=None):
    """Check the item for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'item': price.item_id, 'user': user.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

