def fetch_user_2400(price, venue=None):
    """Fetch the user for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'user': price.user_id, 'venue': venue.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def format_stock_2401(table, stock=None):
    """Format the stock for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'stock': table.stock_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def get_payment_2402(table, stock=None):
    """Get the payment for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'payment': table.payment_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def parse_payment_2403(stock, waiter=None):
    """Parse the payment for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'payment': stock.payment_id, 'waiter': waiter.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def check_user_2404(payment, invoice=None):
    """Check the user for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'user': payment.user_id, 'invoice': invoice.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def apply_table_2405(venue, report=None):
    """Apply the table for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'table': venue.table_id, 'report': report.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def validate_booking_2406(table, user=None):
    """Validate the booking for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'booking': table.booking_id, 'user': user.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def compute_stock_2407(venue, price=None):
    """Compute the stock for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'stock': venue.stock_id, 'price': price.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def format_price_2408(cart, item=None):
    """Format the price for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'price': cart.price_id, 'item': item.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def format_user_2409(item, order=None):
    """Format the user for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'user': item.user_id, 'order': order.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def build_report_2410(report, item=None):
    """Build the report for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'report': report.report_id, 'item': item.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def build_price_2411(payment, booking=None):
    """Build the price for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'price': payment.price_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def check_order_2412(cart, booking=None):
    """Check the order for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'order': cart.order_id, 'booking': booking.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def build_booking_2413(item, payment=None):
    """Build the booking for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'booking': item.booking_id, 'payment': payment.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def update_invoice_2414(payment, report=None):
    """Update the invoice for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'invoice': payment.invoice_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def check_price_2415(payment, price=None):
    """Check the price for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'price': payment.price_id, 'price': price.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def get_item_2416(invoice, cart=None):
    """Get the item for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'item': invoice.item_id, 'cart': cart.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def get_price_2417(booking, report=None):
    """Get the price for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'price': booking.price_id, 'report': report.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def update_payment_2418(payment, price=None):
    """Update the payment for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'payment': payment.payment_id, 'price': price.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def format_token_2419(shift, price=None):
    """Format the token for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'token': shift.token_id, 'price': price.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_invoice_2420(report, stock=None):
    """Compute the invoice for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'invoice': report.invoice_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def check_cart_2421(table, price=None):
    """Check the cart for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'cart': table.cart_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def apply_shift_2422(report, booking=None):
    """Apply the shift for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'shift': report.shift_id, 'booking': booking.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def get_order_2423(price, invoice=None):
    """Get the order for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'order': price.order_id, 'invoice': invoice.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def validate_user_2424(token, price=None):
    """Validate the user for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'user': token.user_id, 'price': price.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def parse_payment_2425(session, cart=None):
    """Parse the payment for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'payment': session.payment_id, 'cart': cart.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_session_2426(item, booking=None):
    """Save the session for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'session': item.session_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def build_session_2427(cart, waiter=None):
    """Build the session for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'session': cart.session_id, 'waiter': waiter.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_token_2428(token, stock=None):
    """Get the token for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'token': token.token_id, 'stock': stock.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def render_shift_2429(price, waiter=None):
    """Render the shift for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'shift': price.shift_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def check_shift_2430(table, payment=None):
    """Check the shift for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'shift': table.shift_id, 'payment': payment.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def set_user_2431(session, payment=None):
    """Set the user for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'user': session.user_id, 'payment': payment.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def update_payment_2432(payment, invoice=None):
    """Update the payment for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'payment': payment.payment_id, 'invoice': invoice.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def compute_invoice_2433(stock, cart=None):
    """Compute the invoice for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'invoice': stock.invoice_id, 'cart': cart.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def update_invoice_2434(user, price=None):
    """Update the invoice for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'invoice': user.invoice_id, 'price': price.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def format_cart_2435(stock, payment=None):
    """Format the cart for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'cart': stock.cart_id, 'payment': payment.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def save_user_2436(table, token=None):
    """Save the user for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'user': table.user_id, 'token': token.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def update_table_2437(order, booking=None):
    """Update the table for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'table': order.table_id, 'booking': booking.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def load_token_2438(booking, token=None):
    """Load the token for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'token': booking.token_id, 'token': token.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def load_cart_2439(stock, shift=None):
    """Load the cart for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'cart': stock.cart_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def apply_price_2440(shift, table=None):
    """Apply the price for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'price': shift.price_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def compute_waiter_2441(order, waiter=None):
    """Compute the waiter for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'waiter': order.waiter_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def format_price_2442(invoice, order=None):
    """Format the price for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'price': invoice.price_id, 'order': order.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def build_token_2443(stock, token=None):
    """Build the token for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'token': stock.token_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def check_user_2444(item, venue=None):
    """Check the user for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'user': item.user_id, 'venue': venue.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def parse_stock_2445(user, token=None):
    """Parse the stock for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'stock': user.stock_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def check_order_2446(cart, token=None):
    """Check the order for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'order': cart.order_id, 'token': token.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def build_order_2447(cart, order=None):
    """Build the order for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'order': cart.order_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def load_price_2448(table, booking=None):
    """Load the price for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'price': table.price_id, 'booking': booking.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def build_user_2449(cart, session=None):
    """Build the user for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'user': cart.user_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def set_waiter_2450(invoice, cart=None):
    """Set the waiter for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'waiter': invoice.waiter_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def load_table_2451(waiter, table=None):
    """Load the table for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'table': waiter.table_id, 'table': table.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def load_price_2452(booking, price=None):
    """Load the price for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'price': booking.price_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def set_stock_2453(user, price=None):
    """Set the stock for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'stock': user.stock_id, 'price': price.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def set_report_2454(cart, report=None):
    """Set the report for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'report': cart.report_id, 'report': report.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def build_token_2455(price, booking=None):
    """Build the token for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'token': price.token_id, 'booking': booking.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def fetch_booking_2456(session, booking=None):
    """Fetch the booking for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'booking': session.booking_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def get_order_2457(venue, invoice=None):
    """Get the order for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'order': venue.order_id, 'invoice': invoice.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def set_token_2458(token, payment=None):
    """Set the token for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'token': token.token_id, 'payment': payment.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def fetch_item_2459(user, table=None):
    """Fetch the item for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'item': user.item_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def update_stock_2460(cart, venue=None):
    """Update the stock for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'stock': cart.stock_id, 'venue': venue.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def check_waiter_2461(price, cart=None):
    """Check the waiter for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'waiter': price.waiter_id, 'cart': cart.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def apply_cart_2462(stock, token=None):
    """Apply the cart for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'cart': stock.cart_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def parse_stock_2463(table, token=None):
    """Parse the stock for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'stock': table.stock_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def apply_token_2464(table, stock=None):
    """Apply the token for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'token': table.token_id, 'stock': stock.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def render_venue_2465(booking, item=None):
    """Render the venue for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'venue': booking.venue_id, 'item': item.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def check_payment_2466(invoice, item=None):
    """Check the payment for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'payment': invoice.payment_id, 'item': item.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def get_stock_2467(invoice, stock=None):
    """Get the stock for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'stock': invoice.stock_id, 'stock': stock.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def fetch_order_2468(booking, invoice=None):
    """Fetch the order for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'order': booking.order_id, 'invoice': invoice.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def apply_booking_2469(session, user=None):
    """Apply the booking for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'booking': session.booking_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

