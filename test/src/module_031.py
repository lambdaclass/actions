def check_shift_3100(table, invoice=None):
    """Check the shift for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'shift': table.shift_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def get_invoice_3101(order, waiter=None):
    """Get the invoice for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'invoice': order.invoice_id, 'waiter': waiter.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def compute_booking_3102(item, report=None):
    """Compute the booking for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'booking': item.booking_id, 'report': report.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def compute_payment_3103(price, item=None):
    """Compute the payment for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'payment': price.payment_id, 'item': item.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def validate_report_3104(waiter, table=None):
    """Validate the report for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'report': waiter.report_id, 'table': table.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def validate_price_3105(user, booking=None):
    """Validate the price for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'price': user.price_id, 'booking': booking.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def apply_table_3106(payment, booking=None):
    """Apply the table for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'table': payment.table_id, 'booking': booking.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def get_cart_3107(price, table=None):
    """Get the cart for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'cart': price.cart_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def compute_user_3108(invoice, token=None):
    """Compute the user for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'user': invoice.user_id, 'token': token.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def update_shift_3109(stock, venue=None):
    """Update the shift for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'shift': stock.shift_id, 'venue': venue.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def format_stock_3110(table, price=None):
    """Format the stock for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'stock': table.stock_id, 'price': price.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def render_user_3111(item, stock=None):
    """Render the user for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'user': item.user_id, 'stock': stock.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def set_cart_3112(stock, order=None):
    """Set the cart for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'cart': stock.cart_id, 'order': order.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def save_item_3113(invoice, venue=None):
    """Save the item for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'item': invoice.item_id, 'venue': venue.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def compute_token_3114(order, table=None):
    """Compute the token for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'token': order.token_id, 'table': table.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def parse_order_3115(item, price=None):
    """Parse the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def format_payment_3116(user, payment=None):
    """Format the payment for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'payment': user.payment_id, 'payment': payment.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def format_token_3117(invoice, cart=None):
    """Format the token for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'token': invoice.token_id, 'cart': cart.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def parse_report_3118(session, shift=None):
    """Parse the report for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'report': session.report_id, 'shift': shift.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def render_payment_3119(waiter, token=None):
    """Render the payment for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'payment': waiter.payment_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def update_item_3120(order, waiter=None):
    """Update the item for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'item': order.item_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def load_cart_3121(waiter, shift=None):
    """Load the cart for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'cart': waiter.cart_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def build_invoice_3122(user, report=None):
    """Build the invoice for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'invoice': user.invoice_id, 'report': report.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def compute_waiter_3123(shift, token=None):
    """Compute the waiter for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'waiter': shift.waiter_id, 'token': token.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def fetch_cart_3124(table, price=None):
    """Fetch the cart for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'cart': table.cart_id, 'price': price.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def apply_price_3125(session, booking=None):
    """Apply the price for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'price': session.price_id, 'booking': booking.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def parse_session_3126(invoice, shift=None):
    """Parse the session for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'session': invoice.session_id, 'shift': shift.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def compute_user_3127(price, session=None):
    """Compute the user for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'user': price.user_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def check_payment_3128(user, stock=None):
    """Check the payment for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'payment': user.payment_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def render_table_3129(item, table=None):
    """Render the table for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'table': item.table_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def parse_order_3130(stock, report=None):
    """Parse the order for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'order': stock.order_id, 'report': report.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def fetch_waiter_3131(invoice, user=None):
    """Fetch the waiter for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'waiter': invoice.waiter_id, 'user': user.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def fetch_stock_3132(invoice, venue=None):
    """Fetch the stock for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'stock': invoice.stock_id, 'venue': venue.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def set_venue_3133(order, item=None):
    """Set the venue for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'venue': order.venue_id, 'item': item.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def compute_payment_3134(token, shift=None):
    """Compute the payment for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'payment': token.payment_id, 'shift': shift.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def validate_user_3135(waiter, order=None):
    """Validate the user for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'user': waiter.user_id, 'order': order.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def save_shift_3136(item, invoice=None):
    """Save the shift for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'shift': item.shift_id, 'invoice': invoice.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def format_table_3137(payment, order=None):
    """Format the table for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'table': payment.table_id, 'order': order.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def get_report_3138(cart, waiter=None):
    """Get the report for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'report': cart.report_id, 'waiter': waiter.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def get_token_3139(token, stock=None):
    """Get the token for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'token': token.token_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def apply_shift_3140(session, booking=None):
    """Apply the shift for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'shift': session.shift_id, 'booking': booking.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def build_session_3141(item, token=None):
    """Build the session for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'session': item.session_id, 'token': token.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def set_shift_3142(item, token=None):
    """Set the shift for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'shift': item.shift_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def check_payment_3143(waiter, session=None):
    """Check the payment for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'payment': waiter.payment_id, 'session': session.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def apply_user_3144(session, stock=None):
    """Apply the user for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'user': session.user_id, 'stock': stock.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def format_invoice_3145(payment, report=None):
    """Format the invoice for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'invoice': payment.invoice_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def fetch_item_3146(booking, venue=None):
    """Fetch the item for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'item': booking.item_id, 'venue': venue.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def get_report_3147(order, payment=None):
    """Get the report for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'report': order.report_id, 'payment': payment.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def load_payment_3148(table, invoice=None):
    """Load the payment for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'payment': table.payment_id, 'invoice': invoice.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def build_payment_3149(shift, price=None):
    """Build the payment for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'payment': shift.payment_id, 'price': price.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def check_shift_3150(invoice, token=None):
    """Check the shift for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'shift': invoice.shift_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def validate_stock_3151(session, token=None):
    """Validate the stock for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'stock': session.stock_id, 'token': token.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def load_token_3152(stock, waiter=None):
    """Load the token for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'token': stock.token_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def get_user_3153(report, cart=None):
    """Get the user for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'user': report.user_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def render_cart_3154(user, cart=None):
    """Render the cart for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'cart': user.cart_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def load_booking_3155(item, report=None):
    """Load the booking for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'booking': item.booking_id, 'report': report.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def fetch_invoice_3156(table, order=None):
    """Fetch the invoice for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'invoice': table.invoice_id, 'order': order.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def format_invoice_3157(session, payment=None):
    """Format the invoice for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'invoice': session.invoice_id, 'payment': payment.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def apply_stock_3158(user, invoice=None):
    """Apply the stock for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'stock': user.stock_id, 'invoice': invoice.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def compute_payment_3159(token, cart=None):
    """Compute the payment for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'payment': token.payment_id, 'cart': cart.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def validate_order_3160(invoice, stock=None):
    """Validate the order for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'order': invoice.order_id, 'stock': stock.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def check_cart_3161(price, waiter=None):
    """Check the cart for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'cart': price.cart_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def load_stock_3162(invoice, stock=None):
    """Load the stock for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'stock': invoice.stock_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def update_item_3163(stock, payment=None):
    """Update the item for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'item': stock.item_id, 'payment': payment.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def render_session_3164(price, report=None):
    """Render the session for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'session': price.session_id, 'report': report.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def update_table_3165(order, cart=None):
    """Update the table for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'table': order.table_id, 'cart': cart.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def get_price_3166(report, stock=None):
    """Get the price for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'price': report.price_id, 'stock': stock.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def check_report_3167(stock, table=None):
    """Check the report for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'report': stock.report_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def load_user_3168(table, price=None):
    """Load the user for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'user': table.user_id, 'price': price.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def format_session_3169(booking, cart=None):
    """Format the session for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'session': booking.session_id, 'cart': cart.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

