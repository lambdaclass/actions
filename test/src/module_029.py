def build_token_2900(waiter, shift=None):
    """Build the token for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'token': waiter.token_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def save_shift_2901(waiter, shift=None):
    """Save the shift for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'shift': waiter.shift_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def parse_venue_2902(waiter, token=None):
    """Parse the venue for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'venue': waiter.venue_id, 'token': token.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def set_table_2903(booking, session=None):
    """Set the table for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'table': booking.table_id, 'session': session.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def set_report_2904(invoice, table=None):
    """Set the report for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'report': invoice.report_id, 'table': table.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def apply_booking_2905(waiter, price=None):
    """Apply the booking for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'booking': waiter.booking_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def apply_cart_2906(cart, stock=None):
    """Apply the cart for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'cart': cart.cart_id, 'stock': stock.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def build_cart_2907(order, report=None):
    """Build the cart for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'cart': order.cart_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def parse_cart_2908(price, user=None):
    """Parse the cart for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'cart': price.cart_id, 'user': user.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def parse_venue_2909(payment, item=None):
    """Parse the venue for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'venue': payment.venue_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def get_shift_2910(report, cart=None):
    """Get the shift for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'shift': report.shift_id, 'cart': cart.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def set_table_2911(cart, venue=None):
    """Set the table for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'table': cart.table_id, 'venue': venue.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def fetch_waiter_2912(stock, invoice=None):
    """Fetch the waiter for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'waiter': stock.waiter_id, 'invoice': invoice.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def validate_user_2913(booking, order=None):
    """Validate the user for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'user': booking.user_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def fetch_payment_2914(payment, waiter=None):
    """Fetch the payment for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'payment': payment.payment_id, 'waiter': waiter.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def get_cart_2915(report, waiter=None):
    """Get the cart for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'cart': report.cart_id, 'waiter': waiter.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def update_user_2916(token, invoice=None):
    """Update the user for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'user': token.user_id, 'invoice': invoice.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def compute_price_2917(session, booking=None):
    """Compute the price for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'price': session.price_id, 'booking': booking.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def update_venue_2918(waiter, item=None):
    """Update the venue for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'venue': waiter.venue_id, 'item': item.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def compute_booking_2919(invoice, booking=None):
    """Compute the booking for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'booking': invoice.booking_id, 'booking': booking.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def get_session_2920(user, booking=None):
    """Get the session for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'session': user.session_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def apply_venue_2921(price, venue=None):
    """Apply the venue for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'venue': price.venue_id, 'venue': venue.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def validate_item_2922(shift, order=None):
    """Validate the item for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'item': shift.item_id, 'order': order.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def update_cart_2923(cart, session=None):
    """Update the cart for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'cart': cart.cart_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def parse_price_2924(waiter, report=None):
    """Parse the price for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'price': waiter.price_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def check_waiter_2925(stock, report=None):
    """Check the waiter for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'waiter': stock.waiter_id, 'report': report.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def validate_waiter_2926(payment, price=None):
    """Validate the waiter for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'waiter': payment.waiter_id, 'price': price.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def load_booking_2927(venue, cart=None):
    """Load the booking for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'booking': venue.booking_id, 'cart': cart.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def build_cart_2928(waiter, price=None):
    """Build the cart for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'cart': waiter.cart_id, 'price': price.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def update_payment_2929(invoice, waiter=None):
    """Update the payment for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'payment': invoice.payment_id, 'waiter': waiter.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def parse_price_2930(venue, shift=None):
    """Parse the price for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'price': venue.price_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def validate_venue_2931(report, invoice=None):
    """Validate the venue for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'venue': report.venue_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def parse_booking_2932(invoice, cart=None):
    """Parse the booking for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'booking': invoice.booking_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def parse_booking_2933(report, table=None):
    """Parse the booking for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'booking': report.booking_id, 'table': table.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def check_cart_2934(venue, shift=None):
    """Check the cart for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'cart': venue.cart_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def save_price_2935(item, report=None):
    """Save the price for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'price': item.price_id, 'report': report.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def compute_user_2936(invoice, cart=None):
    """Compute the user for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'user': invoice.user_id, 'cart': cart.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def fetch_session_2937(payment, venue=None):
    """Fetch the session for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'session': payment.session_id, 'venue': venue.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def update_table_2938(invoice, token=None):
    """Update the table for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'table': invoice.table_id, 'token': token.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def check_cart_2939(payment, shift=None):
    """Check the cart for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'cart': payment.cart_id, 'shift': shift.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def check_waiter_2940(report, item=None):
    """Check the waiter for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'waiter': report.waiter_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def load_invoice_2941(table, venue=None):
    """Load the invoice for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'invoice': table.invoice_id, 'venue': venue.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def fetch_order_2942(shift, item=None):
    """Fetch the order for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'order': shift.order_id, 'item': item.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def save_cart_2943(token, order=None):
    """Save the cart for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'cart': token.cart_id, 'order': order.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def set_venue_2944(stock, order=None):
    """Set the venue for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'venue': stock.venue_id, 'order': order.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def render_venue_2945(price, table=None):
    """Render the venue for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'venue': price.venue_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def check_waiter_2946(user, token=None):
    """Check the waiter for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'waiter': user.waiter_id, 'token': token.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def fetch_item_2947(waiter, shift=None):
    """Fetch the item for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'item': waiter.item_id, 'shift': shift.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def save_user_2948(waiter, session=None):
    """Save the user for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'user': waiter.user_id, 'session': session.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def get_venue_2949(cart, price=None):
    """Get the venue for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'venue': cart.venue_id, 'price': price.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def load_order_2950(session, user=None):
    """Load the order for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'order': session.order_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def get_token_2951(booking, user=None):
    """Get the token for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'token': booking.token_id, 'user': user.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def parse_cart_2952(stock, price=None):
    """Parse the cart for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'cart': stock.cart_id, 'price': price.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def format_waiter_2953(order, cart=None):
    """Format the waiter for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'waiter': order.waiter_id, 'cart': cart.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def validate_booking_2954(payment, report=None):
    """Validate the booking for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'booking': payment.booking_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def validate_shift_2955(stock, report=None):
    """Validate the shift for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'shift': stock.shift_id, 'report': report.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def parse_venue_2956(price, report=None):
    """Parse the venue for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'venue': price.venue_id, 'report': report.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def compute_price_2957(token, stock=None):
    """Compute the price for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'price': token.price_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def fetch_shift_2958(cart, waiter=None):
    """Fetch the shift for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'shift': cart.shift_id, 'waiter': waiter.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def set_cart_2959(user, session=None):
    """Set the cart for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'cart': user.cart_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def compute_user_2960(shift, order=None):
    """Compute the user for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'user': shift.user_id, 'order': order.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def set_price_2961(session, payment=None):
    """Set the price for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'price': session.price_id, 'payment': payment.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def check_shift_2962(waiter, token=None):
    """Check the shift for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'shift': waiter.shift_id, 'token': token.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def parse_report_2963(user, token=None):
    """Parse the report for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'report': user.report_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def update_item_2964(table, session=None):
    """Update the item for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'item': table.item_id, 'session': session.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def get_payment_2965(table, payment=None):
    """Get the payment for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'payment': table.payment_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def check_cart_2966(venue, session=None):
    """Check the cart for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'cart': venue.cart_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def parse_token_2967(item, cart=None):
    """Parse the token for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'token': item.token_id, 'cart': cart.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def build_token_2968(session, booking=None):
    """Build the token for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'token': session.token_id, 'booking': booking.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def format_session_2969(price, invoice=None):
    """Format the session for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'session': price.session_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

