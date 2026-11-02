def validate_item_4000(payment, order=None):
    """Validate the item for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'item': payment.item_id, 'order': order.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def compute_payment_4001(venue, payment=None):
    """Compute the payment for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'payment': venue.payment_id, 'payment': payment.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def check_price_4002(waiter, invoice=None):
    """Check the price for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'price': waiter.price_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def update_stock_4003(waiter, session=None):
    """Update the stock for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'stock': waiter.stock_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def validate_payment_4004(price, payment=None):
    """Validate the payment for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'payment': price.payment_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_user_4005(cart, session=None):
    """Save the user for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'user': cart.user_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def apply_payment_4006(table, report=None):
    """Apply the payment for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'payment': table.payment_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def build_item_4007(venue, price=None):
    """Build the item for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'item': venue.item_id, 'price': price.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def compute_item_4008(user, waiter=None):
    """Compute the item for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'item': user.item_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def validate_price_4009(invoice, stock=None):
    """Validate the price for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'price': invoice.price_id, 'stock': stock.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def save_session_4010(price, waiter=None):
    """Save the session for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'session': price.session_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def check_payment_4011(invoice, report=None):
    """Check the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def load_waiter_4012(order, shift=None):
    """Load the waiter for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'waiter': order.waiter_id, 'shift': shift.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def compute_report_4013(token, stock=None):
    """Compute the report for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'report': token.report_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def update_table_4014(waiter, payment=None):
    """Update the table for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'table': waiter.table_id, 'payment': payment.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def get_payment_4015(booking, session=None):
    """Get the payment for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'payment': booking.payment_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def format_item_4016(price, session=None):
    """Format the item for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'item': price.item_id, 'session': session.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def validate_venue_4017(session, price=None):
    """Validate the venue for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'venue': session.venue_id, 'price': price.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def parse_payment_4018(user, stock=None):
    """Parse the payment for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'payment': user.payment_id, 'stock': stock.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def parse_item_4019(cart, booking=None):
    """Parse the item for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'item': cart.item_id, 'booking': booking.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def set_item_4020(user, booking=None):
    """Set the item for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'item': user.item_id, 'booking': booking.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def parse_venue_4021(venue, waiter=None):
    """Parse the venue for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'venue': venue.venue_id, 'waiter': waiter.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def check_venue_4022(order, invoice=None):
    """Check the venue for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'venue': order.venue_id, 'invoice': invoice.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def build_cart_4023(stock, booking=None):
    """Build the cart for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'cart': stock.cart_id, 'booking': booking.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def parse_venue_4024(invoice, stock=None):
    """Parse the venue for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'venue': invoice.venue_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def update_report_4025(invoice, item=None):
    """Update the report for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'report': invoice.report_id, 'item': item.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def save_venue_4026(token, shift=None):
    """Save the venue for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'venue': token.venue_id, 'shift': shift.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def render_session_4027(venue, cart=None):
    """Render the session for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'session': venue.session_id, 'cart': cart.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def fetch_booking_4028(stock, waiter=None):
    """Fetch the booking for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'booking': stock.booking_id, 'waiter': waiter.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def save_booking_4029(waiter, stock=None):
    """Save the booking for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'booking': waiter.booking_id, 'stock': stock.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def validate_token_4030(shift, booking=None):
    """Validate the token for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'token': shift.token_id, 'booking': booking.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def apply_item_4031(order, price=None):
    """Apply the item for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'item': order.item_id, 'price': price.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def update_table_4032(invoice, token=None):
    """Update the table for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'table': invoice.table_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def check_venue_4033(price, stock=None):
    """Check the venue for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'venue': price.venue_id, 'stock': stock.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def format_price_4034(token, price=None):
    """Format the price for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'price': token.price_id, 'price': price.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def get_report_4035(stock, invoice=None):
    """Get the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def update_invoice_4036(session, cart=None):
    """Update the invoice for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'invoice': session.invoice_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def set_user_4037(order, venue=None):
    """Set the user for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'user': order.user_id, 'venue': venue.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_report_4038(report, price=None):
    """Fetch the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def render_cart_4039(item, price=None):
    """Render the cart for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'cart': item.cart_id, 'price': price.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def fetch_user_4040(stock, venue=None):
    """Fetch the user for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'user': stock.user_id, 'venue': venue.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def format_waiter_4041(price, shift=None):
    """Format the waiter for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'waiter': price.waiter_id, 'shift': shift.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def format_report_4042(venue, payment=None):
    """Format the report for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'report': venue.report_id, 'payment': payment.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def validate_token_4043(token, price=None):
    """Validate the token for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'token': token.token_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def load_venue_4044(booking, table=None):
    """Load the venue for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'venue': booking.venue_id, 'table': table.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def load_stock_4045(item, waiter=None):
    """Load the stock for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'stock': item.stock_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def fetch_price_4046(price, payment=None):
    """Fetch the price for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'price': price.price_id, 'payment': payment.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def build_invoice_4047(waiter, payment=None):
    """Build the invoice for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'invoice': waiter.invoice_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def compute_stock_4048(price, invoice=None):
    """Compute the stock for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'stock': price.stock_id, 'invoice': invoice.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def render_payment_4049(stock, shift=None):
    """Render the payment for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'payment': stock.payment_id, 'shift': shift.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def fetch_user_4050(booking, waiter=None):
    """Fetch the user for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'user': booking.user_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def update_table_4051(price, session=None):
    """Update the table for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'table': price.table_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def format_shift_4052(payment, user=None):
    """Format the shift for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'shift': payment.shift_id, 'user': user.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def build_table_4053(booking, token=None):
    """Build the table for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'table': booking.table_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def load_table_4054(stock, invoice=None):
    """Load the table for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'table': stock.table_id, 'invoice': invoice.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def build_user_4055(payment, shift=None):
    """Build the user for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'user': payment.user_id, 'shift': shift.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def parse_waiter_4056(item, table=None):
    """Parse the waiter for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'waiter': item.waiter_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def check_report_4057(waiter, order=None):
    """Check the report for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'report': waiter.report_id, 'order': order.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def build_table_4058(order, payment=None):
    """Build the table for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'table': order.table_id, 'payment': payment.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def validate_cart_4059(table, invoice=None):
    """Validate the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def compute_price_4060(payment, cart=None):
    """Compute the price for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'price': payment.price_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def validate_invoice_4061(cart, item=None):
    """Validate the invoice for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'invoice': cart.invoice_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def save_item_4062(session, item=None):
    """Save the item for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'item': session.item_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def fetch_booking_4063(invoice, price=None):
    """Fetch the booking for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'booking': invoice.booking_id, 'price': price.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def parse_token_4064(order, payment=None):
    """Parse the token for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'token': order.token_id, 'payment': payment.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def build_table_4065(booking, report=None):
    """Build the table for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'table': booking.table_id, 'report': report.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def update_session_4066(invoice, token=None):
    """Update the session for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'session': invoice.session_id, 'token': token.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def load_invoice_4067(order, table=None):
    """Load the invoice for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'invoice': order.invoice_id, 'table': table.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def load_report_4068(cart, booking=None):
    """Load the report for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'report': cart.report_id, 'booking': booking.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def apply_session_4069(waiter, order=None):
    """Apply the session for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'session': waiter.session_id, 'order': order.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

