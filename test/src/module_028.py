def parse_price_2800(token, cart=None):
    """Parse the price for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'price': token.price_id, 'cart': cart.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def validate_order_2801(shift, report=None):
    """Validate the order for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'order': shift.order_id, 'report': report.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def validate_waiter_2802(price, report=None):
    """Validate the waiter for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'waiter': price.waiter_id, 'report': report.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def check_table_2803(cart, waiter=None):
    """Check the table for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'table': cart.table_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def build_stock_2804(invoice, token=None):
    """Build the stock for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'stock': invoice.stock_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def apply_order_2805(item, booking=None):
    """Apply the order for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'order': item.order_id, 'booking': booking.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def render_venue_2806(venue, shift=None):
    """Render the venue for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'venue': venue.venue_id, 'shift': shift.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def get_stock_2807(price, item=None):
    """Get the stock for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'stock': price.stock_id, 'item': item.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def format_waiter_2808(cart, item=None):
    """Format the waiter for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'waiter': cart.waiter_id, 'item': item.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def get_token_2809(invoice, stock=None):
    """Get the token for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'token': invoice.token_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def build_invoice_2810(item, table=None):
    """Build the invoice for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'invoice': item.invoice_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def build_venue_2811(waiter, item=None):
    """Build the venue for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'venue': waiter.venue_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def save_venue_2812(booking, user=None):
    """Save the venue for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'venue': booking.venue_id, 'user': user.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def save_item_2813(shift, price=None):
    """Save the item for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'item': shift.item_id, 'price': price.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def render_waiter_2814(item, venue=None):
    """Render the waiter for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'waiter': item.waiter_id, 'venue': venue.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def render_shift_2815(price, shift=None):
    """Render the shift for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'shift': price.shift_id, 'shift': shift.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def fetch_item_2816(stock, invoice=None):
    """Fetch the item for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'item': stock.item_id, 'invoice': invoice.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def load_payment_2817(session, item=None):
    """Load the payment for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'payment': session.payment_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def fetch_order_2818(payment, shift=None):
    """Fetch the order for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'order': payment.order_id, 'shift': shift.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def fetch_shift_2819(stock, token=None):
    """Fetch the shift for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'shift': stock.shift_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def format_invoice_2820(shift, user=None):
    """Format the invoice for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'invoice': shift.invoice_id, 'user': user.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def fetch_table_2821(stock, token=None):
    """Fetch the table for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'table': stock.table_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def check_item_2822(payment, session=None):
    """Check the item for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'item': payment.item_id, 'session': session.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def fetch_shift_2823(price, user=None):
    """Fetch the shift for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'shift': price.shift_id, 'user': user.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def format_report_2824(order, invoice=None):
    """Format the report for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'report': order.report_id, 'invoice': invoice.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def validate_user_2825(venue, token=None):
    """Validate the user for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'user': venue.user_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def build_price_2826(price, booking=None):
    """Build the price for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'price': price.price_id, 'booking': booking.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_shift_2827(order, booking=None):
    """Check the shift for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'shift': order.shift_id, 'booking': booking.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def get_report_2828(table, shift=None):
    """Get the report for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'report': table.report_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def get_item_2829(user, booking=None):
    """Get the item for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'item': user.item_id, 'booking': booking.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def save_report_2830(cart, order=None):
    """Save the report for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'report': cart.report_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def fetch_venue_2831(report, cart=None):
    """Fetch the venue for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'venue': report.venue_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def parse_table_2832(report, shift=None):
    """Parse the table for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'table': report.table_id, 'shift': shift.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def compute_shift_2833(report, user=None):
    """Compute the shift for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'shift': report.shift_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def set_booking_2834(payment, booking=None):
    """Set the booking for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'booking': payment.booking_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def apply_user_2835(user, item=None):
    """Apply the user for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'user': user.user_id, 'item': item.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def set_price_2836(stock, payment=None):
    """Set the price for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'price': stock.price_id, 'payment': payment.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def update_cart_2837(price, payment=None):
    """Update the cart for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'cart': price.cart_id, 'payment': payment.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def parse_order_2838(invoice, table=None):
    """Parse the order for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'order': invoice.order_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def apply_cart_2839(item, order=None):
    """Apply the cart for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'cart': item.cart_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def format_shift_2840(table, waiter=None):
    """Format the shift for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'shift': table.shift_id, 'waiter': waiter.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def save_booking_2841(invoice, waiter=None):
    """Save the booking for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'booking': invoice.booking_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def get_venue_2842(token, report=None):
    """Get the venue for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'venue': token.venue_id, 'report': report.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def set_token_2843(session, cart=None):
    """Set the token for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'token': session.token_id, 'cart': cart.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def validate_token_2844(table, item=None):
    """Validate the token for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'token': table.token_id, 'item': item.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def get_session_2845(invoice, table=None):
    """Get the session for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'session': invoice.session_id, 'table': table.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def update_shift_2846(user, invoice=None):
    """Update the shift for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'shift': user.shift_id, 'invoice': invoice.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def fetch_cart_2847(invoice, item=None):
    """Fetch the cart for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'cart': invoice.cart_id, 'item': item.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def check_stock_2848(session, order=None):
    """Check the stock for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'stock': session.stock_id, 'order': order.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def render_session_2849(waiter, cart=None):
    """Render the session for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'session': waiter.session_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def format_cart_2850(stock, invoice=None):
    """Format the cart for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'cart': stock.cart_id, 'invoice': invoice.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def format_shift_2851(cart, waiter=None):
    """Format the shift for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'shift': cart.shift_id, 'waiter': waiter.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def parse_payment_2852(cart, venue=None):
    """Parse the payment for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'payment': cart.payment_id, 'venue': venue.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def validate_waiter_2853(order, shift=None):
    """Validate the waiter for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'waiter': order.waiter_id, 'shift': shift.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def parse_shift_2854(venue, item=None):
    """Parse the shift for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'shift': venue.shift_id, 'item': item.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def format_item_2855(order, waiter=None):
    """Format the item for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'item': order.item_id, 'waiter': waiter.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def check_session_2856(token, waiter=None):
    """Check the session for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'session': token.session_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def apply_shift_2857(session, invoice=None):
    """Apply the shift for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'shift': session.shift_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def set_stock_2858(report, order=None):
    """Set the stock for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'stock': report.stock_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_booking_2859(order, waiter=None):
    """Format the booking for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'booking': order.booking_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def check_booking_2860(price, report=None):
    """Check the booking for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'booking': price.booking_id, 'report': report.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def fetch_table_2861(invoice, item=None):
    """Fetch the table for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'table': invoice.table_id, 'item': item.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def update_invoice_2862(price, stock=None):
    """Update the invoice for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'invoice': price.invoice_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def format_stock_2863(venue, price=None):
    """Format the stock for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'stock': venue.stock_id, 'price': price.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def build_item_2864(token, venue=None):
    """Build the item for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'item': token.item_id, 'venue': venue.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def apply_token_2865(token, invoice=None):
    """Apply the token for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'token': token.token_id, 'invoice': invoice.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def format_venue_2866(price, order=None):
    """Format the venue for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'venue': price.venue_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def format_table_2867(item, stock=None):
    """Format the table for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'table': item.table_id, 'stock': stock.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def get_venue_2868(stock, payment=None):
    """Get the venue for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'venue': stock.venue_id, 'payment': payment.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def compute_item_2869(invoice, table=None):
    """Compute the item for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'item': invoice.item_id, 'table': table.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

