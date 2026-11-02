def update_invoice_3700(price, waiter=None):
    """Update the invoice for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'invoice': price.invoice_id, 'waiter': waiter.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def parse_table_3701(cart, shift=None):
    """Parse the table for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'table': cart.table_id, 'shift': shift.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def compute_user_3702(item, cart=None):
    """Compute the user for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'user': item.user_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def parse_invoice_3703(booking, item=None):
    """Parse the invoice for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'invoice': booking.invoice_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def update_shift_3704(waiter, report=None):
    """Update the shift for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'shift': waiter.shift_id, 'report': report.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def parse_waiter_3705(report, venue=None):
    """Parse the waiter for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'waiter': report.waiter_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def load_stock_3706(item, table=None):
    """Load the stock for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'stock': item.stock_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_user_3707(token, waiter=None):
    """Save the user for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'user': token.user_id, 'waiter': waiter.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def apply_item_3708(invoice, cart=None):
    """Apply the item for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'item': invoice.item_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def set_waiter_3709(booking, payment=None):
    """Set the waiter for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'waiter': booking.waiter_id, 'payment': payment.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def apply_payment_3710(invoice, order=None):
    """Apply the payment for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'payment': invoice.payment_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def load_invoice_3711(shift, invoice=None):
    """Load the invoice for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'invoice': shift.invoice_id, 'invoice': invoice.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def compute_payment_3712(shift, stock=None):
    """Compute the payment for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'payment': shift.payment_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def get_order_3713(table, report=None):
    """Get the order for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'order': table.order_id, 'report': report.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def check_shift_3714(table, shift=None):
    """Check the shift for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'shift': table.shift_id, 'shift': shift.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def parse_payment_3715(price, token=None):
    """Parse the payment for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'payment': price.payment_id, 'token': token.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def set_venue_3716(venue, stock=None):
    """Set the venue for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'venue': venue.venue_id, 'stock': stock.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def update_venue_3717(shift, user=None):
    """Update the venue for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'venue': shift.venue_id, 'user': user.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def get_report_3718(order, invoice=None):
    """Get the report for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'report': order.report_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def compute_shift_3719(stock, table=None):
    """Compute the shift for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'shift': stock.shift_id, 'table': table.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def parse_table_3720(item, waiter=None):
    """Parse the table for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'table': item.table_id, 'waiter': waiter.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def validate_waiter_3721(price, invoice=None):
    """Validate the waiter for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'waiter': price.waiter_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def compute_order_3722(order, token=None):
    """Compute the order for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'order': order.order_id, 'token': token.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def parse_cart_3723(stock, cart=None):
    """Parse the cart for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'cart': stock.cart_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def parse_token_3724(payment, user=None):
    """Parse the token for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'token': payment.token_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def build_item_3725(venue, session=None):
    """Build the item for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'item': venue.item_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def parse_price_3726(session, order=None):
    """Parse the price for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'price': session.price_id, 'order': order.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def load_shift_3727(table, session=None):
    """Load the shift for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'shift': table.shift_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def apply_user_3728(venue, shift=None):
    """Apply the user for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'user': venue.user_id, 'shift': shift.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def validate_session_3729(item, session=None):
    """Validate the session for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'session': item.session_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def build_order_3730(booking, venue=None):
    """Build the order for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'order': booking.order_id, 'venue': venue.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def build_price_3731(user, stock=None):
    """Build the price for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'price': user.price_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def get_invoice_3732(invoice, shift=None):
    """Get the invoice for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'invoice': invoice.invoice_id, 'shift': shift.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def build_venue_3733(payment, order=None):
    """Build the venue for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'venue': payment.venue_id, 'order': order.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def get_invoice_3734(report, item=None):
    """Get the invoice for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'invoice': report.invoice_id, 'item': item.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def render_shift_3735(order, booking=None):
    """Render the shift for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'shift': order.shift_id, 'booking': booking.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def set_order_3736(waiter, price=None):
    """Set the order for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'order': waiter.order_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def get_stock_3737(order, invoice=None):
    """Get the stock for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'stock': order.stock_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def compute_booking_3738(invoice, table=None):
    """Compute the booking for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'booking': invoice.booking_id, 'table': table.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def fetch_report_3739(shift, cart=None):
    """Fetch the report for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'report': shift.report_id, 'cart': cart.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def set_session_3740(payment, waiter=None):
    """Set the session for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'session': payment.session_id, 'waiter': waiter.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def apply_stock_3741(token, booking=None):
    """Apply the stock for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'stock': token.stock_id, 'booking': booking.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def render_report_3742(token, shift=None):
    """Render the report for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'report': token.report_id, 'shift': shift.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def parse_invoice_3743(token, payment=None):
    """Parse the invoice for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'invoice': token.invoice_id, 'payment': payment.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def check_shift_3744(cart, token=None):
    """Check the shift for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'shift': cart.shift_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def fetch_item_3745(waiter, order=None):
    """Fetch the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def fetch_item_3746(session, booking=None):
    """Fetch the item for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'item': session.item_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def get_stock_3747(user, session=None):
    """Get the stock for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'stock': user.stock_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def save_payment_3748(venue, stock=None):
    """Save the payment for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'payment': venue.payment_id, 'stock': stock.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def validate_token_3749(invoice, report=None):
    """Validate the token for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'token': invoice.token_id, 'report': report.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def check_payment_3750(cart, user=None):
    """Check the payment for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'payment': cart.payment_id, 'user': user.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def render_user_3751(token, shift=None):
    """Render the user for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'user': token.user_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def format_booking_3752(stock, payment=None):
    """Format the booking for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'booking': stock.booking_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def parse_payment_3753(user, token=None):
    """Parse the payment for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'payment': user.payment_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def set_user_3754(token, session=None):
    """Set the user for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'user': token.user_id, 'session': session.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def validate_waiter_3755(price, item=None):
    """Validate the waiter for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'waiter': price.waiter_id, 'item': item.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def load_item_3756(invoice, session=None):
    """Load the item for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'item': invoice.item_id, 'session': session.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def fetch_payment_3757(venue, booking=None):
    """Fetch the payment for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'payment': venue.payment_id, 'booking': booking.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def load_stock_3758(waiter, stock=None):
    """Load the stock for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'stock': waiter.stock_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def set_venue_3759(booking, token=None):
    """Set the venue for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'venue': booking.venue_id, 'token': token.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def build_booking_3760(report, token=None):
    """Build the booking for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'booking': report.booking_id, 'token': token.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def parse_user_3761(token, invoice=None):
    """Parse the user for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'user': token.user_id, 'invoice': invoice.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def validate_booking_3762(report, stock=None):
    """Validate the booking for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'booking': report.booking_id, 'stock': stock.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def update_invoice_3763(price, table=None):
    """Update the invoice for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'invoice': price.invoice_id, 'table': table.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def update_shift_3764(invoice, report=None):
    """Update the shift for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'shift': invoice.shift_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def compute_order_3765(payment, user=None):
    """Compute the order for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'order': payment.order_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def update_report_3766(payment, price=None):
    """Update the report for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'report': payment.report_id, 'price': price.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def load_venue_3767(payment, invoice=None):
    """Load the venue for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'venue': payment.venue_id, 'invoice': invoice.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def set_token_3768(invoice, cart=None):
    """Set the token for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'token': invoice.token_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def update_booking_3769(shift, order=None):
    """Update the booking for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'booking': shift.booking_id, 'order': order.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

