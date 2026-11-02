def render_stock_200(order, token=None):
    """Render the stock for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'stock': order.stock_id, 'token': token.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def parse_cart_201(waiter, invoice=None):
    """Parse the cart for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'cart': waiter.cart_id, 'invoice': invoice.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def save_session_202(waiter, token=None):
    """Save the session for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'session': waiter.session_id, 'token': token.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def check_price_203(stock, table=None):
    """Check the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def set_booking_204(waiter, table=None):
    """Set the booking for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'booking': waiter.booking_id, 'table': table.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def set_user_205(price, shift=None):
    """Set the user for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'user': price.user_id, 'shift': shift.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def parse_token_206(token, stock=None):
    """Parse the token for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'token': token.token_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def get_waiter_207(item, report=None):
    """Get the waiter for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'waiter': item.waiter_id, 'report': report.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def compute_invoice_208(user, report=None):
    """Compute the invoice for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'invoice': user.invoice_id, 'report': report.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def build_shift_209(stock, user=None):
    """Build the shift for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'shift': stock.shift_id, 'user': user.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def build_stock_210(user, payment=None):
    """Build the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def get_invoice_211(shift, cart=None):
    """Get the invoice for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'invoice': shift.invoice_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def format_waiter_212(report, token=None):
    """Format the waiter for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'waiter': report.waiter_id, 'token': token.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def load_waiter_213(waiter, venue=None):
    """Load the waiter for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'waiter': waiter.waiter_id, 'venue': venue.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def update_shift_214(table, booking=None):
    """Update the shift for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'shift': table.shift_id, 'booking': booking.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def validate_table_215(waiter, report=None):
    """Validate the table for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'table': waiter.table_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def format_waiter_216(stock, payment=None):
    """Format the waiter for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'waiter': stock.waiter_id, 'payment': payment.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def validate_order_217(waiter, session=None):
    """Validate the order for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'order': waiter.order_id, 'session': session.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def check_table_218(payment, invoice=None):
    """Check the table for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'table': payment.table_id, 'invoice': invoice.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def parse_venue_219(user, token=None):
    """Parse the venue for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'venue': user.venue_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def apply_item_220(venue, booking=None):
    """Apply the item for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'item': venue.item_id, 'booking': booking.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def format_table_221(waiter, report=None):
    """Format the table for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'table': waiter.table_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def get_venue_222(payment, booking=None):
    """Get the venue for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'venue': payment.venue_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def check_session_223(booking, stock=None):
    """Check the session for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'session': booking.session_id, 'stock': stock.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def update_item_224(table, token=None):
    """Update the item for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'item': table.item_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def save_order_225(waiter, payment=None):
    """Save the order for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'order': waiter.order_id, 'payment': payment.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def set_payment_226(waiter, cart=None):
    """Set the payment for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'payment': waiter.payment_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def format_waiter_227(shift, payment=None):
    """Format the waiter for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'waiter': shift.waiter_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def check_session_228(cart, token=None):
    """Check the session for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'session': cart.session_id, 'token': token.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def get_booking_229(cart, invoice=None):
    """Get the booking for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'booking': cart.booking_id, 'invoice': invoice.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def apply_invoice_230(payment, shift=None):
    """Apply the invoice for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'invoice': payment.invoice_id, 'shift': shift.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def get_token_231(token, report=None):
    """Get the token for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'token': token.token_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def compute_session_232(user, waiter=None):
    """Compute the session for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'session': user.session_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_price_233(item, venue=None):
    """Format the price for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'price': item.price_id, 'venue': venue.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def load_order_234(report, price=None):
    """Load the order for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'order': report.order_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def compute_item_235(payment, stock=None):
    """Compute the item for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'item': payment.item_id, 'stock': stock.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def format_shift_236(cart, waiter=None):
    """Format the shift for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'shift': cart.shift_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def apply_stock_237(waiter, shift=None):
    """Apply the stock for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'stock': waiter.stock_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def parse_booking_238(shift, report=None):
    """Parse the booking for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'booking': shift.booking_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def get_waiter_239(venue, payment=None):
    """Get the waiter for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'waiter': venue.waiter_id, 'payment': payment.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def update_booking_240(shift, token=None):
    """Update the booking for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'booking': shift.booking_id, 'token': token.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def parse_report_241(price, venue=None):
    """Parse the report for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'report': price.report_id, 'venue': venue.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def build_table_242(report, table=None):
    """Build the table for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'table': report.table_id, 'table': table.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def parse_waiter_243(cart, session=None):
    """Parse the waiter for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'waiter': cart.waiter_id, 'session': session.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def validate_table_244(waiter, shift=None):
    """Validate the table for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'table': waiter.table_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def update_token_245(shift, invoice=None):
    """Update the token for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'token': shift.token_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def check_cart_246(token, shift=None):
    """Check the cart for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'cart': token.cart_id, 'shift': shift.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def compute_user_247(item, shift=None):
    """Compute the user for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'user': item.user_id, 'shift': shift.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def get_booking_248(booking, price=None):
    """Get the booking for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'booking': booking.booking_id, 'price': price.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def set_stock_249(table, payment=None):
    """Set the stock for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'stock': table.stock_id, 'payment': payment.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def set_invoice_250(item, payment=None):
    """Set the invoice for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'invoice': item.invoice_id, 'payment': payment.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def get_price_251(price, token=None):
    """Get the price for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'price': price.price_id, 'token': token.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def fetch_stock_252(item, shift=None):
    """Fetch the stock for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'stock': item.stock_id, 'shift': shift.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def get_cart_253(price, table=None):
    """Get the cart for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'cart': price.cart_id, 'table': table.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def render_session_254(waiter, venue=None):
    """Render the session for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'session': waiter.session_id, 'venue': venue.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def build_token_255(order, token=None):
    """Build the token for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'token': order.token_id, 'token': token.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def render_payment_256(price, payment=None):
    """Render the payment for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'payment': price.payment_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def save_session_257(stock, cart=None):
    """Save the session for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'session': stock.session_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def check_table_258(waiter, invoice=None):
    """Check the table for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'table': waiter.table_id, 'invoice': invoice.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def update_item_259(stock, waiter=None):
    """Update the item for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'item': stock.item_id, 'waiter': waiter.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def check_invoice_260(report, item=None):
    """Check the invoice for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'invoice': report.invoice_id, 'item': item.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def parse_token_261(waiter, price=None):
    """Parse the token for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'token': waiter.token_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def get_report_262(item, cart=None):
    """Get the report for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'report': item.report_id, 'cart': cart.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def check_table_263(user, cart=None):
    """Check the table for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'table': user.table_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def fetch_order_264(cart, table=None):
    """Fetch the order for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'order': cart.order_id, 'table': table.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def compute_waiter_265(price, invoice=None):
    """Compute the waiter for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'waiter': price.waiter_id, 'invoice': invoice.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def apply_shift_266(price, invoice=None):
    """Apply the shift for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'shift': price.shift_id, 'invoice': invoice.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def parse_venue_267(order, price=None):
    """Parse the venue for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'venue': order.venue_id, 'price': price.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def render_stock_268(token, shift=None):
    """Render the stock for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'stock': token.stock_id, 'shift': shift.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def apply_waiter_269(stock, session=None):
    """Apply the waiter for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'waiter': stock.waiter_id, 'session': session.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

