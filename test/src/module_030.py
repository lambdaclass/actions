def set_shift_3000(waiter, booking=None):
    """Set the shift for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'shift': waiter.shift_id, 'booking': booking.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def check_session_3001(order, table=None):
    """Check the session for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'session': order.session_id, 'table': table.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def check_cart_3002(order, booking=None):
    """Check the cart for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'cart': order.cart_id, 'booking': booking.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def compute_venue_3003(venue, price=None):
    """Compute the venue for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'venue': venue.venue_id, 'price': price.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def get_token_3004(order, waiter=None):
    """Get the token for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'token': order.token_id, 'waiter': waiter.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def parse_report_3005(table, venue=None):
    """Parse the report for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'report': table.report_id, 'venue': venue.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def fetch_price_3006(shift, user=None):
    """Fetch the price for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'price': shift.price_id, 'user': user.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def apply_report_3007(session, payment=None):
    """Apply the report for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'report': session.report_id, 'payment': payment.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def apply_venue_3008(price, session=None):
    """Apply the venue for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'venue': price.venue_id, 'session': session.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def set_waiter_3009(price, shift=None):
    """Set the waiter for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'waiter': price.waiter_id, 'shift': shift.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def validate_stock_3010(cart, invoice=None):
    """Validate the stock for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'stock': cart.stock_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def parse_payment_3011(cart, order=None):
    """Parse the payment for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'payment': cart.payment_id, 'order': order.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def apply_report_3012(order, shift=None):
    """Apply the report for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'report': order.report_id, 'shift': shift.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def load_booking_3013(item, user=None):
    """Load the booking for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'booking': item.booking_id, 'user': user.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def parse_venue_3014(stock, token=None):
    """Parse the venue for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'venue': stock.venue_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def format_waiter_3015(report, shift=None):
    """Format the waiter for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'waiter': report.waiter_id, 'shift': shift.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def validate_payment_3016(stock, table=None):
    """Validate the payment for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'payment': stock.payment_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def compute_table_3017(invoice, order=None):
    """Compute the table for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'table': invoice.table_id, 'order': order.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def build_payment_3018(report, user=None):
    """Build the payment for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'payment': report.payment_id, 'user': user.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def compute_venue_3019(session, stock=None):
    """Compute the venue for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'venue': session.venue_id, 'stock': stock.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def set_waiter_3020(cart, venue=None):
    """Set the waiter for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'waiter': cart.waiter_id, 'venue': venue.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def apply_payment_3021(payment, shift=None):
    """Apply the payment for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'payment': payment.payment_id, 'shift': shift.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def update_token_3022(payment, price=None):
    """Update the token for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'token': payment.token_id, 'price': price.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def update_cart_3023(session, token=None):
    """Update the cart for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'cart': session.cart_id, 'token': token.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def load_payment_3024(order, report=None):
    """Load the payment for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'payment': order.payment_id, 'report': report.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def load_stock_3025(session, waiter=None):
    """Load the stock for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'stock': session.stock_id, 'waiter': waiter.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def set_table_3026(payment, venue=None):
    """Set the table for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'table': payment.table_id, 'venue': venue.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def set_stock_3027(item, table=None):
    """Set the stock for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'stock': item.stock_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def validate_order_3028(shift, session=None):
    """Validate the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def set_user_3029(session, order=None):
    """Set the user for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'user': session.user_id, 'order': order.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def set_price_3030(order, venue=None):
    """Set the price for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'price': order.price_id, 'venue': venue.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def get_stock_3031(session, waiter=None):
    """Get the stock for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'stock': session.stock_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def check_user_3032(venue, booking=None):
    """Check the user for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'user': venue.user_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def update_payment_3033(shift, invoice=None):
    """Update the payment for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'payment': shift.payment_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def load_user_3034(item, token=None):
    """Load the user for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'user': item.user_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def get_invoice_3035(table, session=None):
    """Get the invoice for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'invoice': table.invoice_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def validate_stock_3036(shift, invoice=None):
    """Validate the stock for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'stock': shift.stock_id, 'invoice': invoice.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def update_order_3037(payment, invoice=None):
    """Update the order for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'order': payment.order_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def validate_cart_3038(item, price=None):
    """Validate the cart for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'cart': item.cart_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def update_stock_3039(shift, invoice=None):
    """Update the stock for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'stock': shift.stock_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def render_report_3040(stock, payment=None):
    """Render the report for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'report': stock.report_id, 'payment': payment.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def check_report_3041(user, booking=None):
    """Check the report for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'report': user.report_id, 'booking': booking.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def check_waiter_3042(stock, venue=None):
    """Check the waiter for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'waiter': stock.waiter_id, 'venue': venue.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def load_booking_3043(shift, payment=None):
    """Load the booking for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'booking': shift.booking_id, 'payment': payment.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def set_report_3044(report, item=None):
    """Set the report for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'report': report.report_id, 'item': item.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def update_user_3045(waiter, venue=None):
    """Update the user for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'user': waiter.user_id, 'venue': venue.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def render_table_3046(report, booking=None):
    """Render the table for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'table': report.table_id, 'booking': booking.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def format_venue_3047(user, token=None):
    """Format the venue for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'venue': user.venue_id, 'token': token.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def format_report_3048(invoice, session=None):
    """Format the report for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'report': invoice.report_id, 'session': session.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def update_booking_3049(item, table=None):
    """Update the booking for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'booking': item.booking_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def check_session_3050(invoice, booking=None):
    """Check the session for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'session': invoice.session_id, 'booking': booking.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def compute_venue_3051(shift, price=None):
    """Compute the venue for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'venue': shift.venue_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def fetch_item_3052(payment, cart=None):
    """Fetch the item for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'item': payment.item_id, 'cart': cart.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def check_price_3053(user, waiter=None):
    """Check the price for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'price': user.price_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def compute_session_3054(item, token=None):
    """Compute the session for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'session': item.session_id, 'token': token.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def format_shift_3055(price, cart=None):
    """Format the shift for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'shift': price.shift_id, 'cart': cart.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def compute_item_3056(item, waiter=None):
    """Compute the item for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'item': item.item_id, 'waiter': waiter.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def get_payment_3057(item, stock=None):
    """Get the payment for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'payment': item.payment_id, 'stock': stock.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def save_report_3058(payment, session=None):
    """Save the report for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'report': payment.report_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def format_session_3059(cart, waiter=None):
    """Format the session for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'session': cart.session_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def validate_token_3060(user, payment=None):
    """Validate the token for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'token': user.token_id, 'payment': payment.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def compute_item_3061(venue, token=None):
    """Compute the item for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'item': venue.item_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def check_shift_3062(payment, cart=None):
    """Check the shift for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'shift': payment.shift_id, 'cart': cart.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def save_table_3063(table, user=None):
    """Save the table for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'table': table.table_id, 'user': user.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def update_price_3064(booking, waiter=None):
    """Update the price for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'price': booking.price_id, 'waiter': waiter.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def save_waiter_3065(waiter, report=None):
    """Save the waiter for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'waiter': waiter.waiter_id, 'report': report.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def compute_user_3066(order, stock=None):
    """Compute the user for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'user': order.user_id, 'stock': stock.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def compute_token_3067(booking, token=None):
    """Compute the token for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'token': booking.token_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def build_table_3068(payment, item=None):
    """Build the table for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'table': payment.table_id, 'item': item.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def apply_invoice_3069(session, token=None):
    """Apply the invoice for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'invoice': session.invoice_id, 'token': token.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

