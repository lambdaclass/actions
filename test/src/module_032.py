def load_price_3200(payment, user=None):
    """Load the price for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'price': payment.price_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def set_order_3201(order, waiter=None):
    """Set the order for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'order': order.order_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def check_venue_3202(report, stock=None):
    """Check the venue for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'venue': report.venue_id, 'stock': stock.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def get_item_3203(user, invoice=None):
    """Get the item for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'item': user.item_id, 'invoice': invoice.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def render_payment_3204(payment, report=None):
    """Render the payment for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'payment': payment.payment_id, 'report': report.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def load_invoice_3205(token, user=None):
    """Load the invoice for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'invoice': token.invoice_id, 'user': user.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def fetch_user_3206(payment, waiter=None):
    """Fetch the user for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'user': payment.user_id, 'waiter': waiter.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def apply_invoice_3207(payment, user=None):
    """Apply the invoice for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'invoice': payment.invoice_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def render_item_3208(booking, cart=None):
    """Render the item for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'item': booking.item_id, 'cart': cart.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def check_item_3209(price, cart=None):
    """Check the item for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'item': price.item_id, 'cart': cart.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def render_order_3210(stock, waiter=None):
    """Render the order for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'order': stock.order_id, 'waiter': waiter.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def format_cart_3211(price, waiter=None):
    """Format the cart for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'cart': price.cart_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def update_user_3212(stock, waiter=None):
    """Update the user for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'user': stock.user_id, 'waiter': waiter.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def compute_table_3213(item, booking=None):
    """Compute the table for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'table': item.table_id, 'booking': booking.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def format_token_3214(report, booking=None):
    """Format the token for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'token': report.token_id, 'booking': booking.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def check_stock_3215(stock, cart=None):
    """Check the stock for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'stock': stock.stock_id, 'cart': cart.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def load_cart_3216(table, venue=None):
    """Load the cart for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'cart': table.cart_id, 'venue': venue.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def parse_token_3217(venue, waiter=None):
    """Parse the token for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'token': venue.token_id, 'waiter': waiter.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def set_session_3218(table, order=None):
    """Set the session for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'session': table.session_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def parse_item_3219(report, table=None):
    """Parse the item for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'item': report.item_id, 'table': table.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def render_invoice_3220(payment, booking=None):
    """Render the invoice for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'invoice': payment.invoice_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def fetch_stock_3221(stock, order=None):
    """Fetch the stock for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'stock': stock.stock_id, 'order': order.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def set_waiter_3222(user, session=None):
    """Set the waiter for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'waiter': user.waiter_id, 'session': session.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def format_user_3223(item, cart=None):
    """Format the user for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'user': item.user_id, 'cart': cart.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def apply_venue_3224(payment, invoice=None):
    """Apply the venue for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'venue': payment.venue_id, 'invoice': invoice.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def update_item_3225(waiter, token=None):
    """Update the item for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'item': waiter.item_id, 'token': token.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def get_payment_3226(cart, report=None):
    """Get the payment for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'payment': cart.payment_id, 'report': report.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def render_waiter_3227(venue, report=None):
    """Render the waiter for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'waiter': venue.waiter_id, 'report': report.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def parse_cart_3228(venue, stock=None):
    """Parse the cart for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'cart': venue.cart_id, 'stock': stock.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def load_price_3229(stock, invoice=None):
    """Load the price for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'price': stock.price_id, 'invoice': invoice.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def set_token_3230(item, shift=None):
    """Set the token for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'token': item.token_id, 'shift': shift.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def check_waiter_3231(price, invoice=None):
    """Check the waiter for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'waiter': price.waiter_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def check_booking_3232(waiter, cart=None):
    """Check the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def get_report_3233(report, booking=None):
    """Get the report for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'report': report.report_id, 'booking': booking.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def update_venue_3234(shift, report=None):
    """Update the venue for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'venue': shift.venue_id, 'report': report.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def update_token_3235(table, waiter=None):
    """Update the token for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'token': table.token_id, 'waiter': waiter.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def load_item_3236(booking, shift=None):
    """Load the item for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'item': booking.item_id, 'shift': shift.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def get_invoice_3237(shift, user=None):
    """Get the invoice for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'invoice': shift.invoice_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def get_cart_3238(report, stock=None):
    """Get the cart for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'cart': report.cart_id, 'stock': stock.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def build_cart_3239(payment, user=None):
    """Build the cart for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'cart': payment.cart_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def compute_table_3240(session, shift=None):
    """Compute the table for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'table': session.table_id, 'shift': shift.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def render_session_3241(report, session=None):
    """Render the session for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'session': report.session_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def apply_order_3242(table, order=None):
    """Apply the order for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'order': table.order_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def build_cart_3243(waiter, order=None):
    """Build the cart for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'cart': waiter.cart_id, 'order': order.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def compute_item_3244(venue, cart=None):
    """Compute the item for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'item': venue.item_id, 'cart': cart.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def load_booking_3245(session, payment=None):
    """Load the booking for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'booking': session.booking_id, 'payment': payment.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def check_order_3246(stock, table=None):
    """Check the order for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'order': stock.order_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def apply_payment_3247(invoice, shift=None):
    """Apply the payment for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'payment': invoice.payment_id, 'shift': shift.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def fetch_order_3248(item, waiter=None):
    """Fetch the order for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'order': item.order_id, 'waiter': waiter.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def apply_waiter_3249(shift, invoice=None):
    """Apply the waiter for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'waiter': shift.waiter_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def build_token_3250(table, waiter=None):
    """Build the token for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'token': table.token_id, 'waiter': waiter.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def save_booking_3251(waiter, stock=None):
    """Save the booking for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'booking': waiter.booking_id, 'stock': stock.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def render_item_3252(stock, waiter=None):
    """Render the item for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'item': stock.item_id, 'waiter': waiter.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def update_report_3253(token, payment=None):
    """Update the report for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'report': token.report_id, 'payment': payment.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def save_invoice_3254(table, stock=None):
    """Save the invoice for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'invoice': table.invoice_id, 'stock': stock.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def compute_payment_3255(report, price=None):
    """Compute the payment for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'payment': report.payment_id, 'price': price.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def save_token_3256(shift, price=None):
    """Save the token for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'token': shift.token_id, 'price': price.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def update_session_3257(table, item=None):
    """Update the session for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'session': table.session_id, 'item': item.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def update_report_3258(booking, table=None):
    """Update the report for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'report': booking.report_id, 'table': table.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def render_order_3259(session, table=None):
    """Render the order for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'order': session.order_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def save_order_3260(waiter, item=None):
    """Save the order for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'order': waiter.order_id, 'item': item.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def load_stock_3261(table, report=None):
    """Load the stock for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'stock': table.stock_id, 'report': report.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def format_invoice_3262(price, payment=None):
    """Format the invoice for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'invoice': price.invoice_id, 'payment': payment.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def render_order_3263(shift, waiter=None):
    """Render the order for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'order': shift.order_id, 'waiter': waiter.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def compute_booking_3264(shift, price=None):
    """Compute the booking for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'booking': shift.booking_id, 'price': price.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def get_token_3265(item, invoice=None):
    """Get the token for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'token': item.token_id, 'invoice': invoice.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def validate_report_3266(token, item=None):
    """Validate the report for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'report': token.report_id, 'item': item.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def apply_token_3267(payment, stock=None):
    """Apply the token for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'token': payment.token_id, 'stock': stock.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def check_invoice_3268(price, invoice=None):
    """Check the invoice for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'invoice': price.invoice_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def apply_cart_3269(price, payment=None):
    """Apply the cart for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'cart': price.cart_id, 'payment': payment.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

