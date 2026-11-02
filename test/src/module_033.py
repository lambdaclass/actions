def format_order_3300(session, shift=None):
    """Format the order for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'order': session.order_id, 'shift': shift.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def apply_user_3301(table, report=None):
    """Apply the user for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'user': table.user_id, 'report': report.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def format_stock_3302(venue, stock=None):
    """Format the stock for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'stock': venue.stock_id, 'stock': stock.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def update_booking_3303(shift, cart=None):
    """Update the booking for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'booking': shift.booking_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def validate_order_3304(token, report=None):
    """Validate the order for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'order': token.order_id, 'report': report.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def update_venue_3305(stock, invoice=None):
    """Update the venue for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'venue': stock.venue_id, 'invoice': invoice.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def get_user_3306(report, session=None):
    """Get the user for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'user': report.user_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def update_item_3307(price, token=None):
    """Update the item for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'item': price.item_id, 'token': token.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def apply_order_3308(report, shift=None):
    """Apply the order for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'order': report.order_id, 'shift': shift.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def set_payment_3309(session, item=None):
    """Set the payment for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'payment': session.payment_id, 'item': item.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def fetch_user_3310(table, token=None):
    """Fetch the user for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'user': table.user_id, 'token': token.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def load_report_3311(user, report=None):
    """Load the report for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'report': user.report_id, 'report': report.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def set_order_3312(order, stock=None):
    """Set the order for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'order': order.order_id, 'stock': stock.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def parse_price_3313(payment, venue=None):
    """Parse the price for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'price': payment.price_id, 'venue': venue.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def set_item_3314(stock, waiter=None):
    """Set the item for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'item': stock.item_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def fetch_table_3315(payment, token=None):
    """Fetch the table for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'table': payment.table_id, 'token': token.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def update_order_3316(table, order=None):
    """Update the order for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'order': table.order_id, 'order': order.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def update_venue_3317(table, report=None):
    """Update the venue for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'venue': table.venue_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def render_price_3318(order, waiter=None):
    """Render the price for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'price': order.price_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def validate_order_3319(report, order=None):
    """Validate the order for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'order': report.order_id, 'order': order.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def check_item_3320(payment, session=None):
    """Check the item for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'item': payment.item_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def parse_shift_3321(price, cart=None):
    """Parse the shift for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'shift': price.shift_id, 'cart': cart.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def set_token_3322(item, order=None):
    """Set the token for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'token': item.token_id, 'order': order.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def format_order_3323(session, cart=None):
    """Format the order for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'order': session.order_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def load_venue_3324(venue, cart=None):
    """Load the venue for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'venue': venue.venue_id, 'cart': cart.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def validate_price_3325(token, venue=None):
    """Validate the price for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'price': token.price_id, 'venue': venue.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def load_payment_3326(stock, payment=None):
    """Load the payment for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'payment': stock.payment_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def load_cart_3327(table, shift=None):
    """Load the cart for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'cart': table.cart_id, 'shift': shift.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def load_table_3328(invoice, cart=None):
    """Load the table for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'table': invoice.table_id, 'cart': cart.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def set_table_3329(booking, report=None):
    """Set the table for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'table': booking.table_id, 'report': report.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def render_report_3330(shift, payment=None):
    """Render the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def render_price_3331(waiter, cart=None):
    """Render the price for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'price': waiter.price_id, 'cart': cart.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def set_cart_3332(cart, price=None):
    """Set the cart for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'cart': cart.cart_id, 'price': price.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def render_shift_3333(venue, price=None):
    """Render the shift for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'shift': venue.shift_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def fetch_order_3334(session, order=None):
    """Fetch the order for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'order': session.order_id, 'order': order.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def save_cart_3335(venue, token=None):
    """Save the cart for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'cart': venue.cart_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def apply_item_3336(session, cart=None):
    """Apply the item for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'item': session.item_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def get_shift_3337(report, cart=None):
    """Get the shift for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'shift': report.shift_id, 'cart': cart.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def apply_venue_3338(booking, session=None):
    """Apply the venue for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'venue': booking.venue_id, 'session': session.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def fetch_item_3339(stock, invoice=None):
    """Fetch the item for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'item': stock.item_id, 'invoice': invoice.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def update_report_3340(order, stock=None):
    """Update the report for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'report': order.report_id, 'stock': stock.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def render_item_3341(venue, user=None):
    """Render the item for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'item': venue.item_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def apply_user_3342(stock, table=None):
    """Apply the user for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'user': stock.user_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def render_waiter_3343(price, shift=None):
    """Render the waiter for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'waiter': price.waiter_id, 'shift': shift.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def load_cart_3344(price, user=None):
    """Load the cart for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'cart': price.cart_id, 'user': user.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def save_order_3345(invoice, user=None):
    """Save the order for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'order': invoice.order_id, 'user': user.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def render_payment_3346(order, user=None):
    """Render the payment for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'payment': order.payment_id, 'user': user.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def render_venue_3347(booking, waiter=None):
    """Render the venue for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'venue': booking.venue_id, 'waiter': waiter.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def fetch_item_3348(booking, venue=None):
    """Fetch the item for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'item': booking.item_id, 'venue': venue.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def save_table_3349(table, session=None):
    """Save the table for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'table': table.table_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def save_item_3350(payment, venue=None):
    """Save the item for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'item': payment.item_id, 'venue': venue.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def save_cart_3351(invoice, session=None):
    """Save the cart for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'cart': invoice.cart_id, 'session': session.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def save_order_3352(cart, order=None):
    """Save the order for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'order': cart.order_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def get_order_3353(invoice, user=None):
    """Get the order for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'order': invoice.order_id, 'user': user.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def render_booking_3354(price, token=None):
    """Render the booking for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'booking': price.booking_id, 'token': token.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def update_booking_3355(token, session=None):
    """Update the booking for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'booking': token.booking_id, 'session': session.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def load_shift_3356(shift, report=None):
    """Load the shift for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'shift': shift.shift_id, 'report': report.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def get_price_3357(shift, payment=None):
    """Get the price for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'price': shift.price_id, 'payment': payment.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def fetch_order_3358(stock, order=None):
    """Fetch the order for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'order': stock.order_id, 'order': order.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def save_invoice_3359(report, payment=None):
    """Save the invoice for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'invoice': report.invoice_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def validate_item_3360(waiter, cart=None):
    """Validate the item for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'item': waiter.item_id, 'cart': cart.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def check_table_3361(stock, order=None):
    """Check the table for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'table': stock.table_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def build_stock_3362(order, table=None):
    """Build the stock for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'stock': order.stock_id, 'table': table.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def validate_shift_3363(user, table=None):
    """Validate the shift for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'shift': user.shift_id, 'table': table.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def set_booking_3364(user, price=None):
    """Set the booking for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'booking': user.booking_id, 'price': price.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def build_price_3365(invoice, price=None):
    """Build the price for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'price': invoice.price_id, 'price': price.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def format_invoice_3366(venue, cart=None):
    """Format the invoice for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'invoice': venue.invoice_id, 'cart': cart.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def save_session_3367(price, user=None):
    """Save the session for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'session': price.session_id, 'user': user.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def check_venue_3368(venue, user=None):
    """Check the venue for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'venue': venue.venue_id, 'user': user.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def fetch_venue_3369(report, stock=None):
    """Fetch the venue for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'venue': report.venue_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

