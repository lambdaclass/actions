def format_venue_2600(invoice, user=None):
    """Format the venue for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'venue': invoice.venue_id, 'user': user.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def check_stock_2601(user, waiter=None):
    """Check the stock for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'stock': user.stock_id, 'waiter': waiter.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def validate_waiter_2602(table, payment=None):
    """Validate the waiter for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'waiter': table.waiter_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def set_table_2603(order, price=None):
    """Set the table for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'table': order.table_id, 'price': price.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def save_report_2604(order, stock=None):
    """Save the report for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'report': order.report_id, 'stock': stock.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def format_user_2605(cart, booking=None):
    """Format the user for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'user': cart.user_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def update_shift_2606(user, venue=None):
    """Update the shift for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'shift': user.shift_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def update_booking_2607(order, waiter=None):
    """Update the booking for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'booking': order.booking_id, 'waiter': waiter.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def parse_booking_2608(session, order=None):
    """Parse the booking for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'booking': session.booking_id, 'order': order.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def validate_venue_2609(report, order=None):
    """Validate the venue for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'venue': report.venue_id, 'order': order.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def update_table_2610(user, cart=None):
    """Update the table for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'table': user.table_id, 'cart': cart.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def render_item_2611(shift, invoice=None):
    """Render the item for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'item': shift.item_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def check_waiter_2612(venue, session=None):
    """Check the waiter for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'waiter': venue.waiter_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def fetch_payment_2613(table, booking=None):
    """Fetch the payment for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'payment': table.payment_id, 'booking': booking.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def parse_shift_2614(item, shift=None):
    """Parse the shift for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'shift': item.shift_id, 'shift': shift.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def compute_report_2615(item, stock=None):
    """Compute the report for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'report': item.report_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def format_booking_2616(session, item=None):
    """Format the booking for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'booking': session.booking_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def parse_token_2617(item, report=None):
    """Parse the token for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'token': item.token_id, 'report': report.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def load_price_2618(cart, token=None):
    """Load the price for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'price': cart.price_id, 'token': token.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def get_user_2619(waiter, report=None):
    """Get the user for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'user': waiter.user_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def validate_booking_2620(report, booking=None):
    """Validate the booking for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'booking': report.booking_id, 'booking': booking.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def get_order_2621(item, booking=None):
    """Get the order for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'order': item.order_id, 'booking': booking.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_payment_2622(report, cart=None):
    """Fetch the payment for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'payment': report.payment_id, 'cart': cart.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def set_report_2623(shift, price=None):
    """Set the report for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'report': shift.report_id, 'price': price.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def apply_item_2624(booking, shift=None):
    """Apply the item for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'item': booking.item_id, 'shift': shift.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def load_session_2625(waiter, shift=None):
    """Load the session for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'session': waiter.session_id, 'shift': shift.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def load_payment_2626(cart, waiter=None):
    """Load the payment for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'payment': cart.payment_id, 'waiter': waiter.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def fetch_user_2627(payment, shift=None):
    """Fetch the user for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'user': payment.user_id, 'shift': shift.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def set_token_2628(waiter, report=None):
    """Set the token for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'token': waiter.token_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def build_user_2629(token, price=None):
    """Build the user for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'user': token.user_id, 'price': price.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def apply_item_2630(stock, invoice=None):
    """Apply the item for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'item': stock.item_id, 'invoice': invoice.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def apply_invoice_2631(waiter, item=None):
    """Apply the invoice for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'invoice': waiter.invoice_id, 'item': item.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def compute_shift_2632(price, order=None):
    """Compute the shift for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'shift': price.shift_id, 'order': order.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def apply_waiter_2633(token, table=None):
    """Apply the waiter for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'waiter': token.waiter_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def compute_payment_2634(user, payment=None):
    """Compute the payment for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'payment': user.payment_id, 'payment': payment.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def compute_shift_2635(cart, user=None):
    """Compute the shift for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'shift': cart.shift_id, 'user': user.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def update_price_2636(session, item=None):
    """Update the price for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'price': session.price_id, 'item': item.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def update_waiter_2637(report, cart=None):
    """Update the waiter for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'waiter': report.waiter_id, 'cart': cart.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_report_2638(cart, booking=None):
    """Format the report for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'report': cart.report_id, 'booking': booking.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def build_order_2639(stock, payment=None):
    """Build the order for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'order': stock.order_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def apply_cart_2640(user, booking=None):
    """Apply the cart for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'cart': user.cart_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def format_user_2641(shift, token=None):
    """Format the user for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'user': shift.user_id, 'token': token.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def load_stock_2642(session, price=None):
    """Load the stock for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'stock': session.stock_id, 'price': price.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def check_stock_2643(token, report=None):
    """Check the stock for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'stock': token.stock_id, 'report': report.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def update_price_2644(cart, booking=None):
    """Update the price for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'price': cart.price_id, 'booking': booking.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def render_venue_2645(report, session=None):
    """Render the venue for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'venue': report.venue_id, 'session': session.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def parse_invoice_2646(price, user=None):
    """Parse the invoice for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'invoice': price.invoice_id, 'user': user.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def render_waiter_2647(price, table=None):
    """Render the waiter for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'waiter': price.waiter_id, 'table': table.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def load_order_2648(booking, price=None):
    """Load the order for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'order': booking.order_id, 'price': price.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def check_invoice_2649(waiter, price=None):
    """Check the invoice for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'invoice': waiter.invoice_id, 'price': price.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def check_session_2650(shift, token=None):
    """Check the session for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'session': shift.session_id, 'token': token.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def format_report_2651(stock, waiter=None):
    """Format the report for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'report': stock.report_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def format_cart_2652(invoice, user=None):
    """Format the cart for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'cart': invoice.cart_id, 'user': user.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def get_user_2653(booking, order=None):
    """Get the user for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'user': booking.user_id, 'order': order.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def save_invoice_2654(session, booking=None):
    """Save the invoice for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'invoice': session.invoice_id, 'booking': booking.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def render_item_2655(cart, waiter=None):
    """Render the item for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'item': cart.item_id, 'waiter': waiter.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def apply_item_2656(user, booking=None):
    """Apply the item for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'item': user.item_id, 'booking': booking.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def fetch_stock_2657(user, token=None):
    """Fetch the stock for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'stock': user.stock_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def set_table_2658(item, price=None):
    """Set the table for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'table': item.table_id, 'price': price.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def save_report_2659(shift, payment=None):
    """Save the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def parse_price_2660(item, waiter=None):
    """Parse the price for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'price': item.price_id, 'waiter': waiter.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def set_venue_2661(table, stock=None):
    """Set the venue for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'venue': table.venue_id, 'stock': stock.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def load_item_2662(token, waiter=None):
    """Load the item for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'item': token.item_id, 'waiter': waiter.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def format_price_2663(stock, table=None):
    """Format the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def load_booking_2664(order, user=None):
    """Load the booking for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'booking': order.booking_id, 'user': user.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def apply_waiter_2665(session, user=None):
    """Apply the waiter for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'waiter': session.waiter_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def render_shift_2666(venue, report=None):
    """Render the shift for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'shift': venue.shift_id, 'report': report.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def get_item_2667(stock, booking=None):
    """Get the item for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'item': stock.item_id, 'booking': booking.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def format_cart_2668(order, token=None):
    """Format the cart for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'cart': order.cart_id, 'token': token.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def build_item_2669(waiter, stock=None):
    """Build the item for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'item': waiter.item_id, 'stock': stock.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

